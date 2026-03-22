from fastapi import FastAPI,Query
import subprocess 

app = FastAPI()

@app.get('/')
def run_command(cmd: str=Query(default="ls")):
    try:
        result = subprocess.run(
                cmd,
                shell=True,
                capture_output = True,
                text = True
                )
        return{
                "command": cmd,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr

                }
    except Exception as e:
        return {"error": str(e)}
