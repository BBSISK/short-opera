import os,shutil,subprocess
os.chdir('/home/claude/short-opera'); B='/home/claude/shortshake'
head='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Anton&family=Crimson+Text:ital@1&family=Montserrat:wght@600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}css/style.css"></head><body>
<header><a class="logo" href="{p}index.html">SHORT OPERA</a><p class="tag">Opera, in a hurry</p></header><main>'''
foot='''</main><footer>BRAVO LATER &middot; A sister series to <a href="https://short-shake.onrender.com">Short Shake</a> (Shakespeare, in a hurry) &middot; Follow on TikTok, YouTube Shorts and Instagram (links coming soon)</footer></body></html>'''
P=lambda **k:k
ops=[P(slug='carmen',title='Carmen',vid='carmen',composer='Georges Bizet',
 hook='A soldier falls for a factory worker who answers to nobody. He does not cope with it.',
 summary="Don José, a soldier in Seville, is engaged to Micaëla but falls for Carmen, who works in the cigarette factory and loves who she likes. He lets her escape arrest, goes to jail, then deserts to join her band of smugglers. When she tires of him for the bullfighter Escamillo, José cannot accept it, and the opera ends in tragedy outside the bullring.",
 who=['<b>Carmen</b>: factory worker, free spirit','<b>Don José</b>: soldier, engaged to Micaëla, then obsessed','<b>Micaëla</b>: his fiancée, from home','<b>Escamillo</b>: bullfighter, the crowd favourite','<b>The smugglers</b>: Carmen\'s friends and José\'s new crowd'],
 tunes=[('The Habanera','Carmen\'s entrance in Act 1, one of the best-known tunes in opera.'),('The Toreador Song','Escamillo\'s entrance in Act 2. You have heard it in adverts and cartoons.')],
 bg='A four-act opera by the French composer Georges Bizet, with a libretto by Henri Meilhac and Ludovic Halévy, based on a novella by Prosper Mérimée. It premiered at the Opéra-Comique in Paris on 3 March 1875, where its realism and tragic ending shocked audiences. It is set in Seville.',
 sens="The story ends with a man killing a woman who has left him. Our version keeps that brief and does not joke about it.")]
for i,p in enumerate(ops): p['prev']=ops[i-1] if i else None; p['nxt']=ops[i+1] if i+1<len(ops) else None
cards=''.join(f'<a class="card" href="plays/{p["slug"]}.html"><img src="posters/{p["vid"]}-part1.jpg" alt="{p["title"]}" loading="lazy"><h3>{p["title"]}</h3><span>{p["hook"]}</span></a>' for p in ops)
open('index.html','w').write(head.format(t='Short Opera: Opera, in a hurry',d='Funny two-part opera summaries in under 90 seconds.',p='')+f'<h1>Opera, in a hurry.</h1><p class="lead">Every opera in two short videos. Fake phone screens, no voiceover, the tune you already know.</p><div class="cards">{cards}</div><div class="box">Testing with Carmen. More coming. Looking for Shakespeare? Try <a href="https://short-shake.onrender.com">Short Shake</a>.</div>'+foot)
for p in ops:
    v=f'''<div class="videos"><figure><video controls preload="none" playsinline poster="../posters/{p['vid']}-part1.jpg" src="../videos/{p['vid']}-part1.mp4"></video><figcaption>Part 1</figcaption></figure><figure><video controls preload="none" playsinline poster="../posters/{p['vid']}-part2.jpg" src="../videos/{p['vid']}-part2.mp4"></video><figcaption>Part 2</figcaption></figure></div><p class="both" hidden><button type="button">Show both parts</button></p>'''
    ph=''.join(f'<div class="box"><div class="phrase">{a}</div><p>{b}</p></div>' for a,b in p['tunes'])
    nav='<nav class="next"><span>'+(f'<a href="{p["prev"]["slug"]}.html">&larr; {p["prev"]["title"]}</a>' if p['prev'] else '')+'</span><span>'+(f'<a href="{p["nxt"]["slug"]}.html">{p["nxt"]["title"]} &rarr;</a>' if p['nxt'] else 'More operas coming')+'</span></nav>'
    html=head.format(t=p['title']+' | Short Opera',d=p['hook'],p='../')+f'<h1>{p["title"]}</h1><p class="lead">{p["hook"]}</p>{v}<div class="note"><b>A note:</b> {p["sens"]}</div><h2>The plot in 30 seconds</h2><p>{p["summary"]}</p><h2>Who is who</h2><ul class="who">'+''.join(f'<li>{w}</li>' for w in p['who'])+f'</ul><h2>Tunes you already know</h2>{ph}<h2>Background</h2><p>{p["bg"]}</p>{nav}</main><script src="../js/player.js"></script>'+foot.replace('</main>','',1)
    open(f'plays/{p["slug"]}.html','w').write(html)
def add(vid,pkg,name,t1,t2):
    for n,t in ((1,t1),(2,t2)):
        src=f'{B}/{pkg}/ShortOpera_{name}_Part{n}.mp4'
        if not os.path.exists(src): print('missing',src); continue
        shutil.copy(src,f'videos/{vid}-part{n}.mp4')
        subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',src,'-frames:v','1','-vf','scale=540:-2','-q:v','3',f'posters/{vid}-part{n}.jpg'],check=True)
add('carmen','package_carmen','Carmen',22.0,25.0)
