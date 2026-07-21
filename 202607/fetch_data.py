#!/usr/bin/env python3
"""Fetch AI Agent news data from multiple sources."""
import subprocess, json, re, html as html_mod

def curl(url, extra_args="", timeout=15):
    cmd = f"curl -sL --connect-timeout 5 --max-time {timeout} '{url}' {extra_args} 2>/dev/null | head -3000"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout+5)
        return result.stdout
    except subprocess.TimeoutExpired:
        return ""

def fetch_arxiv():
    """Fetch latest AI agent papers from arXiv."""
    html = curl("https://arxiv.org/search/?searchtype=all&query=AI+agent+LLM+agent+agentic+multi-agent&start=0&order=-announced_date_first")
    entries = re.findall(r'<li class="arxiv-result">(.*?)</li>', html, re.DOTALL)
    papers = []
    for entry in entries[:20]:
        title_m = re.search(r'<p class="title is-5 mathjax">\s*(.*?)\s*</p>', entry, re.DOTALL)
        authors_m = re.search(r'<p class="authors">.*?<span[^>]*>(.*?)</span>', entry, re.DOTALL)
        abstract_m = re.search(r'<span class="abstract-full[^"]*">\s*(.*?)\s*</span>', entry, re.DOTALL)
        link_m = re.search(r'<p class="list-title is-inline-block">.*?<a href="(.*?)">arXiv', entry, re.DOTALL)
        date_m = re.search(r'Submitted\s*(\d+\s+\w+,\s*\d{4})', entry)
        
        if title_m:
            paper = {
                'title': html_mod.unescape(re.sub(r'<.*?>', '', title_m.group(1).strip())),
                'authors': html_mod.unescape(re.sub(r'<.*?>', '', authors_m.group(1).strip())) if authors_m else 'N/A',
                'date': date_m.group(1) if date_m else 'N/A',
                'link': 'https://arxiv.org' + link_m.group(1) if link_m else 'N/A',
                'abstract': html_mod.unescape(re.sub(r'<.*?>', '', abstract_m.group(1).strip()[:250])) if abstract_m else 'N/A'
            }
            papers.append(paper)
    return papers

def fetch_hackernews():
    """Fetch HN stories about AI agents."""
    html = curl("https://hn.algolia.com/api/v1/search?query=AI+agent&tags=story&numericFilters=created_at_i>1753440000&hitsPerPage=15")
    try:
        data = json.loads(html)
        hits = data.get('hits', [])
        return [{'title': h.get('title'), 'url': h.get('url'), 'points': h.get('points'), 'comments': h.get('num_comments'), 'date': h.get('created_at')} for h in hits[:15]]
    except:
        return []

def fetch_techcrunch():
    """Fetch TechCrunch AI headlines."""
    html = curl("https://techcrunch.com/category/artificial-intelligence/", "-H 'User-Agent: Mozilla/5.0'")
    # Extract article links
    articles = re.findall(r'<a[^>]*href="(https://techcrunch\.com/\d{4}/\d{2}/\d{2}/[^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
    results = []
    seen = set()
    for url, inner in articles[:15]:
        if url in seen:
            continue
        seen.add(url)
        title = html_mod.unescape(re.sub(r'<.*?>', '', inner.strip()[:200]))
        if len(title) > 20:
            results.append({'title': title, 'url': url})
    return results

def fetch_venturebeat():
    """Fetch VentureBeat AI headlines."""
    html = curl("https://venturebeat.com/category/ai/", "-H 'User-Agent: Mozilla/5.0'")
    articles = re.findall(r'<a[^>]*href="(https://venturebeat\.com/ai/[^"]+)"[^>]*class="ArticleListing__title-link[^"]*"[^>]*>(.*?)</a>', html)
    if not articles:
        articles = re.findall(r'<h[23][^>]*>.*?<a[^>]*href="(https://venturebeat\.com/ai/[^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
    return [{'title': html_mod.unescape(re.sub(r'<.*?>', '', t.strip())), 'url': u} for u, t in articles[:15]]

def fetch_reddit_ml():
    """Fetch Reddit ML hot posts - skip if timeout."""
    return []  # Skip Reddit, often times out

def fetch_theverge():
    """Fetch The Verge AI news."""
    html = curl("https://www.theverge.com/ai-artificial-intelligence", "-H 'User-Agent: Mozilla/5.0'")
    articles = re.findall(r'<a[^>]*href="(https://www\.theverge\.com/[^"]*\d{4}/\d{1,2}/\d{1,2}[^"]*)"[^>]*>(.*?)</a>', html, re.DOTALL)
    results = []
    seen = set()
    for url, inner in articles[:15]:
        if url in seen:
            continue
        seen.add(url)
        title = html_mod.unescape(re.sub(r'<.*?>', '', inner.strip()[:200]))
        if len(title) > 20 and '/ai-' in url.lower() or 'openai' in url.lower() or 'google' in url.lower() or 'agent' in url.lower():
            results.append({'title': title, 'url': url})
    return results

def fetch_jiqizhixin():
    """Fetch 机器之心 news."""
    html = curl("https://www.jiqizhixin.com/", "-H 'User-Agent: Mozilla/5.0'")
    articles = re.findall(r'<a[^>]*href="(/articles/[^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
    return [{'title': html_mod.unescape(re.sub(r'<.*?>', '', t.strip()[:150])), 'url': 'https://www.jiqizhixin.com' + u} for u, t in articles[:15] if len(t.strip()) > 15]

def fetch_qbitai():
    """Fetch 量子位 news."""
    html = curl("https://www.qbitai.com/", "-H 'User-Agent: Mozilla/5.0'")
    articles = re.findall(r'<a[^>]*href="(https?://www\.qbitai\.com/[^"]*\d+[^"]*)"[^>]*>(.*?)</a>', html, re.DOTALL)
    return [{'title': html_mod.unescape(re.sub(r'<.*?>', '', t.strip()[:150])), 'url': u} for u, t in articles[:15] if len(t.strip()) > 15]

def fetch_36kr():
    """Fetch 36氪 AI news."""
    html = curl("https://36kr.com/information/AI/", "-H 'User-Agent: Mozilla/5.0'")
    articles = re.findall(r'<a[^>]*href="(/p/\d+[^"]*)"[^>]*>(.*?)</a>', html, re.DOTALL)
    results = []
    for u, t in articles[:15]:
        title = html_mod.unescape(re.sub(r'<.*?>', '', t.strip()[:150]))
        if len(title) > 10:
            results.append({'title': title, 'url': 'https://36kr.com' + u})
    return results

def fetch_github_trending():
    """Fetch GitHub trending data."""
    html = curl("https://github.com/trending?since=daily")
    repos = re.findall(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    results = []
    for repo in repos[:20]:
        name_m = re.search(r'<h2[^>]*>\s*<a[^>]*href="(/[^/]+/[^"]+)"[^>]*>.*?<span[^>]*>(.*?)</span>', repo, re.DOTALL)
        desc_m = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', repo, re.DOTALL)
        stars_m = re.search(r'(\d[\d,]*)\s+stars today', repo)
        if name_m:
            full_name = name_m.group(1).strip('/')
            results.append({
                'name': full_name,
                'desc': desc_m.group(1).strip() if desc_m else '',
                'url': 'https://github.com' + name_m.group(1),
                'stars_today': stars_m.group(1) if stars_m else '0'
            })
    return results

# Run all fetchers
if __name__ == '__main__':
    import sys
    
    output = {}
    
    fetchers = [
        ('arxiv', fetch_arxiv),
        ('hackernews', fetch_hackernews),
        ('techcrunch', fetch_techcrunch),
        ('venturebeat', fetch_venturebeat),
        ('theverge', fetch_theverge),
        ('jiqizhixin', fetch_jiqizhixin),
        ('qbitai', fetch_qbitai),
        ('36kr', fetch_36kr),
        ('github_trending', fetch_github_trending),
    ]
    
    for name, func in fetchers:
        try:
            print(f"Fetching {name}...", file=sys.stderr)
            output[name] = func()
        except Exception as e:
            print(f"Error fetching {name}: {e}", file=sys.stderr)
            output[name] = []
    
    print(json.dumps(output, ensure_ascii=False, indent=2))
