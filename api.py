from flask import Flask, request, jsonify
import main

app = Flask(__name__)

@app.route('/api/shortlist', methods=['POST'])
def shortlist():
    print("Received request")
    if 'resume' not in request.files:
        print("No resume file found")
        return jsonify({'error': 'No resume file found in the request.'}), 400

    print("Resume file found")
    resume_file = request.files['resume']
    jd = request.form.get('jd')

    if not jd:
        print("No JD found")
        return jsonify({'error': 'No job description found in the request.'}), 400

    print("JD found")
    result = main.process_resume(resume_file, jd)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
