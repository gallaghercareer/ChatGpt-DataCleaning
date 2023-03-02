import os
import datetime
import pdfkit
import pdfplumber
import pypandoc
import praw

def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def convert_pdf_to_txt(pdf_path, txt_path):
    # Extract text from PDF using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    # Convert extracted text to plain text format using pypandoc
    pypandoc.convert_text(text, "plain", format="md", outputfile=txt_path)

    print(f"PDF file '{pdf_path}' converted to TXT file '{txt_path}'")

def scrape_subreddit(subreddit_name, num_days=100):
    # Create directory to store output files
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = f"{subreddit_name}_output_{date_string}"
    os.makedirs(output_dir)

    # Initialize Reddit instance
    reddit = praw.Reddit()

    # Get subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Get submissions for the last num_days
    time_limit = int(datetime.datetime.timestamp(datetime.datetime.utcnow() - datetime.timedelta(days=num_days)))
    submissions = subreddit.submissions(time_limit)

    # Loop through submissions and extract data
    post_counter = 1
    txt_output = ""
    html_output = "<html><body>"
    for submission in submissions:
        print(f"Processing post {post_counter}...")
        post_counter += 1

        # Extract data from submission
        title = submission.title
        author = submission.author.name
        url = submission.url
        selftext = submission.selftext
        date_created = datetime.datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')

        # Add data to text and HTML output
        txt_output += f"TITLE: {title}\n"
        txt_output += f"AUTHOR: {author}\n"
        txt_output += f"URL: {url}\n"
        txt_output += f"DATE CREATED: {date_created}\n"
        txt_output += "\n"
        txt_output += selftext
        txt_output += "\n\n"

        html_output += f"<h1>{title}</h1>"
        html_output += f"<p>AUTHOR: {author}</p>"
        html_output += f"<p>URL: <a href='{url}'>{url}</a></p>"
        html_output += f"<p>DATE CREATED: {date_created}</p>"
        html_output += f"<p>{selftext}</p>"
        html_output += "<hr>"

        # Save submission to PDF
        pdf_filename = f"{output_dir}/post_{post_counter}.pdf"
        pdfkit.from_url(url, pdf_filename)

    # Save text output to file
    txt_filename = f"{output_dir}/output.txt"
    save_file(txt_filename, txt_output)

    # Save HTML output to file
    html_output += "</body></html>"
    html_filename = f"{output_dir}/output.html"
    save_file(html_filename, html_output)

    # Convert PDFs to TXTs and add page breaks
    pdf_files = [f"{output_dir}/{f}" for
