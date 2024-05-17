import logging
import os
from dotenv import load_dotenv
from notion_client import Client
from tqdm import tqdm
from supabase import create_client

load_dotenv()

learning_store_database_id = os.getenv("LEARNING_STORE_DB_ID")
notion_token = os.getenv("notion_token")
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

notion = Client(auth=notion_token)
supabase_client = create_client(supabase_url=supabase_url, supabase_key=supabase_key)

logger = logging.getLogger(__name__)


def get_data(database_id, table_name):
    i = 0
    response = notion.databases.query(database_id=database_id)
    logger.info(f"Got {len(response['results'])} items...")
    batch = []
    for item in tqdm(response["results"]):
        data = {
            "title": item["properties"]["Name"]["title"][0]["plain_text"].strip(),
            "url": item["properties"]["URL"]["url"],
            "type": item["properties"]["Type"]["multi_select"][0]["name"],
            "notion_timestamp": item["created_time"]
        }
        print(f"Appending :: {data}")
        batch.append(data)
    supabase_client.table(table_name).upsert(batch, on_conflict="url").execute()

if __name__ == "__main__":
    logger.info("Starting script...")
    get_data(learning_store_database_id, "LinksStorage")

