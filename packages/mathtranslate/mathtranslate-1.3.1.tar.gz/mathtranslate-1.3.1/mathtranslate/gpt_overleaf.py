import requests
import os


def compile_tex_file(tex_file):
    """
    Compiles a local .tex file to PDF using the Overleaf API.
    Returns the path to the resulting PDF file.
    """
    with open(tex_file, "rb") as f:
        files = {"inputFile": f}
        url = "https://latexonline.cc/compile"
        response = requests.post(url, files=files)
        if response.status_code == 200:
            pdf_file = tex_file.replace(".tex", ".pdf")
            with open(pdf_file, "wb") as f:
                f.write(response.content)
            return pdf_file
        else:
            print(f"Error: {response.status_code}")
            return None


def compile_overleaf_project(api_key, project_id):
    """
    Compiles a local Overleaf project using the Overleaf API.
    Returns the path to the resulting PDF file.
    """
    headers = {"Authorization": f"Bearer {api_key}"}
    url = f"https://api.overleaf.com/project/{project_id}/compile"
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        job_id = response.json()["id"]
        url = f"https://api.overleaf.com/project/{project_id}/compile/{job_id}/status"
        while True:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                if response.json()["status"] == "success":
                    pdf_url = response.json()["output_files"]["main.pdf"]["url"]
                    pdf_file = "main.pdf"
                    with open(pdf_file, "wb") as f:
                        f.write(requests.get(pdf_url).content)
                    return pdf_file
                elif response.json()["status"] == "failure":
                    print(response.json()["error_message"])
                    return None
            else:
                print(f"Error: {response.status_code}")
                return None
    else:
        print(f"Error: {response.status_code}")
        return None
