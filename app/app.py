from flask import Flask, render_template, url_for
import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def execute_shell_script():
    ssh.connect('rdepaiva.tplinkdns.com', username='helladarion', key_filename='/sshkey/id_ed25519_web_patch')
    stdin, stdout, stderr = ssh.exec_command('./script.sh')

    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    ssh.close()
    return output, error


app = Flask(__name__)

@app.route('/')
def home():
    output, err = execute_shell_script()
    return render_template('home.html', title="Web Shell Control", output=output, err=err)
#return f"Hello Rafa!<pre> {output}</pre> <br />Errors:<br /> <pre> {err} </pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

