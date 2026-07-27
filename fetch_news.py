import urllib.request
import json
import sys

# Fetch multiple pages from search_by_date without numeric filters
all_hits = []
for page in range(5):
    url = f"https://hn.algolia.com/api/v1/search_by_date?tags=story&hitsPerPage=200&page={page}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
            for hit in data.get("hits", []):
                created = hit.get("created_at", "")
                if "2026-07-23" in created or "2026-07-24" in created:
                    all_hits.append(hit)
    except Exception as e:
        print(f"Page {page} error: {e}", file=sys.stderr)

# Filter for AI/agent related
keywords = ["AI", "agent", "LLM", "GPT", "Claude", "Gemini", "OpenAI", "Anthropic",
            "model", "reasoning", "RAG", "MCP", "tool", "autonomous", "chatbot",
            "Copilot", "LangChain", "CrewAI", "AutoGen", "Devin", "cursor",
            "deepseek", "Qwen", "Mixtral", "Llama", "Mistral", "Cohere"]

for hit in all_hits:
    title = hit.get("title", "")
    if any(k.lower() in title.lower() for k in keywords):
        obj_id = hit.get("objectID", "")
        url = hit.get("url") or f"https://news.ycombinator.com/item?id={obj_id}"
        print(f"Title: {title}")
        print(f"Created: {hit.get('created_at')}")
        print(f"URL: {url}")
        print(f"Points: {hit.get('points')}, Comments: {hit.get('num_comments')}")
        print("---")

total = len([h for h in all_hits if any(k.lower() in h.get("title", "").lower() for k in keywords)])
print(f"\nTotal relevant: {total}")
print(f"Total in date range: {len(all_hits)}")
