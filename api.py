from flask import Flask, request, jsonify
import main
import traceback

app = Flask(__name__)

@app.route('/api/shortlist', methods=['POST'])
def shortlist():
    print("Received request")

    if 'resume' not in request.files:
        print("❌ No resume file found in request.")
        return jsonify({'error': 'No resume file found in the request.'}), 400

    resume_file = request.files['resume']
    jd = request.form.get('jd')

    if not jd:
        print("❌ No job description found in request.")
        return jsonify({'error': 'No job description found in the request.'}), 400

    print("✅ JD and resume file received. Processing...")

    try:
        result = main.process_resume(resume_file, jd)
        print("✅ Resume processed successfully.")
        return jsonify(result)
    except Exception as e:
        print("🔥 Error during resume processing:")
        traceback.print_exc()
        return jsonify({'error': 'An error occurred while processing the resume.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
