import requests

url = "http://127.0.0.1:5000/api/shortlist"
files = {'resume': open('dummy_resume.pdf', 'rb')}
data = {'jd': """
    🎯 Job Title: AI Intern – Python, TensorFlow, Projects

    We are looking for a recent graduate or final-year student with a strong academic background in Artificial Intelligence. The ideal candidate should have hands-on experience with Python programming and machine learning tools, and have completed academic or internship projects involving model development.

    🔧 Responsibilities:
    - Build predictive models using Scikit-Learn and TensorFlow
    - Analyze datasets using Pandas, NumPy, and Matplotlib
    - Apply machine learning in areas like greenhouse gas (GHG) emissions or plant disease detection
    - Collaborate with mentors in developing model pipelines
    - Work in Linux-based environments with basic AWS and MongoDB knowledge

    ✅ Required Skills:
    - Programming: Python, R, Java, C++
    - Machine Learning: TensorFlow, Scikit-Learn
    - Data Tools: Numpy, Pandas, Matplotlib
    - Databases: SQL, basic MongoDB
    - Cloud: Basic AWS
    - OS: Linux, Windows, Mac
    - Soft Skills: Problem Solving, Team Work, Communication
    - Internship or project experience in AI-based GHG
    """}
response = requests.post(url, files=files, data=data)

print(response.json())
