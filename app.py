from flask import Flask, request, jsonify, render_template
from embedder import embed_texts
from vector_store import search
from llama_runner import ask_llama
import threading
import watcher

app = Flask(__name__)

# Start file watcher in background thread
threading.Thread(target=watcher.start_watching, daemon=True).start()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ask')
def ask():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    embedded = embed_texts([query])[0]
    context = "\n".join(search(embedded))
    answer = ask_llama(context, query)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
