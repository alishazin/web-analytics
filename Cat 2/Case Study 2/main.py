import os.path
import nltk
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set up Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def get_snippets_and_senders(service, max_results=200):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])
    snippets = []
    senders = []

    for msg in messages:
        msg_detail = service.users().messages().get(userId='me', id=msg['id'], format='metadata', metadataHeaders=['From']).execute()
        snippet = msg_detail.get('snippet', '')
        snippets.append(snippet)

        headers = msg_detail.get('payload', {}).get('headers', [])
        for header in headers:
            if header['name'] == 'From':
                senders.append(header['value'])
                break

    return snippets, senders

def analyze_topics(snippets, senders):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    all_text = ' '.join(snippets).lower()

    # Tokenize and POS tag
    tokens = word_tokenize(all_text)
    pos_tags = nltk.pos_tag(tokens)

    # Only keep nouns and verbs, remove stopwords and punctuation
    relevant_words = []
    for word, tag in pos_tags:
        if word.isalpha() and word not in stop_words and len(word) > 3:
            if tag.startswith('NN') or tag.startswith('VB'):
                lemma = lemmatizer.lemmatize(word)
                relevant_words.append(lemma)

    # Count and display most common relevant words
    word_freq = Counter(relevant_words)
    print("\n🔍 Top 20 Relevant Words in Email Snippets:")
    for word, count in word_freq.most_common(20):
        print(f"{word}: {count}")
    
    print("\n🔍 Top 10 most frequent contacts:")
    counter = Counter(senders)
    for sender, count in counter.most_common(10):
        print(f"{sender}: {count} emails")

def main():
    service = authenticate_gmail()
    
    print("📩 Fetching Gmail snippets...")
    snippets, senders = get_snippets_and_senders(service)
    print(f"✅ Fetched {len(snippets)} snippets.")
    
    analyze_topics(snippets, senders)

if __name__ == '__main__':
    main()
