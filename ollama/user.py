import argparse
from ollama import chat
parser = argparse.ArgumentParser(description='Enter Your Query to chatbot')
parser.add_argument("-q","--query",nargs="+",required=True)
args = parser.parse_args()
query = " ".join(args.query)
print(f"Query Provided: {query}")


try:
  stream = chat(
      model = 'qwen2.5:1.5b',
      messages = [{'role':'user','content':query}],
      stream = True,
      options={   # Number of tokens model allowed to generate
        "num_predict": 150
        }
  )

  for chunk in stream:
      print(chunk['message']['content'],end='',flush=True)

  print()

except Exceptions as e:
  print(f"\n[Error] Ollama Failed: {e}")
  sys.exit(2)

