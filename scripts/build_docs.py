"""Generate the public Veepick documentation website and Markdown guides."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
if ROOT.name == 'scripts':
    ROOT = ROOT.parent
BASE = 'https://raoofhassan0-web.github.io/Veepick-docs/'
ICON = 'https://veepick.com/download/assets/veepick-icon.png'
GUIDES = [
    ('getting-started', '01', 'Getting started', 'Your first steps with Veepick, from installing the app to finding your way around.', [
        ('Install Veepick', 'Visit the official Android download page and follow the instructions for your device. If Android asks you to allow an installation, review the source and the system prompt before continuing. Download Veepick only from an official destination linked by Veepick.'),
        ('Create or access your account', 'Open the app and follow the on-screen registration or sign-in steps. Complete any verification requested in the app. Keep your password and sign-in codes to yourself, including when contacting support.'),
        ('Set up your profile', 'Choose your profile name, username and photo using the available profile controls. A recognizable profile makes it easier for people to find the right account. Review what you share before making it visible to others.'),
        ('Explore the app', 'Discover posts and videos, open your conversations, and explore groups or channels. The layout and available options can vary by app version and account. Use the labels and controls shown in your installed version.'),
        ('Make it work for you', 'Review notification, privacy and account settings in the app. Device permissions can be managed in your Android settings. Features such as recording or calling may require the relevant camera or microphone permission.'),
        ('If something does not work', 'Note what you were trying to do, the steps leading to the issue and your app version. Contact support@veepick.com with a short description. A screenshot can help after you hide private information. Never include passwords or verification codes.')]),
    ('sharing-and-messaging', '02', 'Sharing & messaging', 'A practical introduction to posts, videos, stories and everyday conversations.', [
        ('Share a post or video', 'Use the creation controls in the app to select or record content. Review your media, text and available audience options before publishing. Keep the app connected while an upload is in progress and wait for the final publishing confirmation.'),
        ('Understand upload progress', 'An upload indicator reaching 100% may mean the transfer has finished while publishing or media processing is still completing. If the post does not appear or an error is shown, check the result before starting a duplicate upload. Share the error message with support if the issue continues.'),
        ('Use stories and comments', 'Stories offer another way to share updates, while comments keep a conversation connected to a post. Check the controls available on the relevant content for replies, reactions and management options. Only share media you have permission to use.'),
        ('Start a conversation', 'Open an existing conversation or use the app’s available controls to find someone and start a chat. Review the recipient before sending text, media or files. Delivery, read and connection indicators reflect the information currently available to the app.'),
        ('Calls and device permissions', 'Use the call controls available in a supported conversation or community. Android may ask for microphone or camera access when needed. If audio or video is unavailable, check the relevant permission, your connection and the app’s current call state.'),
        ('Manage your experience', 'Use the available notification, blocking, reporting and conversation settings to manage interactions. Available actions depend on the content, your role and the app version. For help with a specific message or upload, include the time and a clear description without exposing private conversations.')]),
    ('communities', '03', 'Groups & channels', 'Understand community spaces, member roles and the controls available to you.', [
        ('Choose the right space', 'Groups support conversations between members. Channels offer a way to publish updates to an audience. Explore the options shown in the app to choose the space that suits your community.'),
        ('Find or join a community', 'Use the available discovery tools, public links or invitations to reach the intended group or channel. Check its name, description and administrators before sharing information. Some communities require an invitation or approval to join.'),
        ('Understand roles and permissions', 'Owners, administrators and members can have different capabilities. Posting, inviting people, managing messages and changing settings depend on the permissions granted in that community. A control may be unavailable if your current role does not permit it.'),
        ('Share and interact', 'Read the community’s description and pinned information before posting. Use replies, comments or reactions where they are available. In a channel, the options for audience participation depend on its configuration.'),
        ('Manage a community', 'If you have the required permissions, use the community management controls to review its details, invitations, members and available moderation settings. Check the effect of an action before applying it to other members or published content.'),
        ('Report an issue', 'Use Report on the relevant content or account where available. Include useful context so a reviewer can locate the issue. If you cannot access the app or complete a report, contact support@veepick.com. Do not send sensitive account credentials.')])]

ICONS = {
 'arrow':'<path d="M5 12h14m-6-6 6 6-6 6"/>',
 'download':'<path d="M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5"/>',
 'book':'<path d="M12 5c-3-2-7-2-10 0v15c3-2 7-2 10 0 3-2 7-2 10 0V5c-3-2-7-2-10 0Zm0 0v15"/>',
 'chat':'<path d="M21 11.5a9 9 0 0 1-9 9 9 9 0 0 1-4-.9L3 21l1.4-5a9 9 0 1 1 16.6-4.5Z"/><path d="M8 10h8M8 14h5"/>',
 'people':'<circle cx="9" cy="8" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3M16 5a3 3 0 0 1 0 6M21 21v-3a6 6 0 0 0-3-5"/>',
 'play':'<rect x="3" y="3" width="18" height="18" rx="5"/><path d="m10 8 6 4-6 4Z"/>',
 'mail':'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
 'github':'<path d="M9 19c-4.3 1.3-4.3-2.2-6-2.7m12 5v-3.5c0-1 .1-1.5-.5-2 3-.4 6-1.5 6-6.5a5 5 0 0 0-1.4-3.5 4.7 4.7 0 0 0-.1-3.5s-1.1-.3-3.5 1.3a12 12 0 0 0-6 0C7.1 2 6 2.3 6 2.3a4.7 4.7 0 0 0-.1 3.5A5 5 0 0 0 4.5 9c0 5 3 6.1 6 6.5-.6.5-.6 1.3-.5 2V21"/>',
 'check':'<path d="m5 12 4 4L19 6"/>',
}
def icon(name):
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+ICONS[name]+'</svg>'
def brand(prefix):
    return '<a class="brand" href="'+prefix+'index.html"><img src="'+ICON+'" alt="" width="34" height="34"><span>Veepick<span class="brand-note"> / Docs</span></span></a>'
def head(title,desc,path,prefix):
    return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="theme-color" content="#ffffff"><title>'+escape(title)+' | Veepick</title><meta name="description" content="'+escape(desc,quote=True)+'"><meta property="og:title" content="'+escape(title,quote=True)+' | Veepick"><meta property="og:description" content="'+escape(desc,quote=True)+'"><meta property="og:type" content="website"><meta property="og:url" content="'+BASE+path+'"><meta property="og:image" content="'+ICON+'"><link rel="canonical" href="'+BASE+path+'"><link rel="icon" href="'+ICON+'"><link rel="stylesheet" href="'+prefix+'styles.css"></head><body id="top"><a class="skip" href="#main">Skip to content</a>'
def header(prefix,active=''):
    return '<header class="site-header"><div class="container header-inner">'+brand(prefix)+'<nav aria-label="Main navigation"><a href="'+prefix+'index.html"'+(' aria-current="page"' if active=='home' else '')+'>Overview</a><a href="'+prefix+'index.html#guides"'+(' aria-current="page"' if active=='guide' else '')+'>Guides</a><a href="'+prefix+'index.html#help">Help</a></nav><a class="header-download" href="https://veepick.com/download/">Get Veepick '+icon('arrow')+'</a></div></header>'
def footer(prefix):
    return '<footer class="site-footer"><div class="container"><div class="footer-grid"><div>'+brand(prefix)+'<p>Your guide to connecting, sharing<br>and finding your community.</p></div><div><h2>Explore</h2><a href="'+prefix+'index.html">Overview</a><a href="'+prefix+'index.html#guides">User guides</a><a href="https://veepick.com/download/">Android download</a></div><div><h2>Keep in touch</h2><a href="https://veepick.com/">Veepick website</a><a href="https://github.com/raoofhassan0-web/Veepick-docs">GitHub documentation</a><a href="mailto:support@veepick.com">support@veepick.com</a></div></div><div class="footer-bottom"><span>© 2026 Veepick</span><nav aria-label="Policies"><a href="https://veepick.com/terms/?lang=en">Terms</a><a href="https://veepick.com/community-guidelines/?lang=en">Community guidelines</a><a href="https://veepick.com/child-safety/?lang=en">Child safety</a><a href="https://veepick.com/delete-account/?lang=en">Account deletion</a><a href="https://veepick.com/privacy/?lang=en">Privacy</a></nav></div></div></footer></body></html>\n'
def guide_cards(prefix=''):
    return ''.join('<a class="guide-card" href="'+prefix+'guides/'+slug+'.html"><span class="guide-no">GUIDE '+num+'</span><span class="guide-icon">'+icon(ico)+'</span><h3>'+title+'</h3><p>'+desc+'</p><span class="read">Read guide '+icon('arrow')+'</span></a>' for (slug,num,title,desc,sections),ico in zip(GUIDES,['book','chat','people']))
def home():
    desc='The official public guide to Veepick. Get started on Android, explore sharing and messaging, and learn about groups and channels.'
    content=head('Documentation',desc,'','')+header('','home')
    content+='''<main id="main"><section class="hero"><div class="container hero-grid"><div class="hero-copy"><div class="eyebrow"><span class="status-dot"></span> THE VEEPICK GUIDE</div><h1>Good conversations.<br>Great communities.<br><span>Start here.</span></h1><p>Get to know Veepick. A place for your videos, everyday conversations and the communities that bring people together.</p><div class="hero-actions"><a class="button primary" href="guides/getting-started.html">Explore the guide '''+icon('arrow')+'''</a><a class="button secondary" href="https://veepick.com/download/">Get Android app '''+icon('download')+'''</a></div><div class="hero-note">Official documentation <span>·</span> In English <span>·</span> No sign-in needed</div></div><div class="hero-visual" aria-hidden="true"><div class="orbit orbit-one"></div><div class="orbit orbit-two"></div><div class="visual-label">A LITTLE CLOSER. A LOT MORE CONNECTED.</div><div class="visual-core"><img src="'''+ICON+'''" alt="" width="72" height="72"><strong>Veepick</strong><span>Bring your world together.</span></div><div class="float-card float-chat"><span class="float-icon">'''+icon('chat')+'''</span><div><strong>Keep the conversation going.</strong><span>Messages & calls</span></div></div><div class="float-card float-video"><span class="float-icon">'''+icon('play')+'''</span><div><strong>A moment worth sharing.</strong><span>Videos, posts & stories</span></div></div><div class="float-card float-community"><span class="float-icon">'''+icon('people')+'''</span><div><strong>Find your people.</strong><span>Groups & channels</span></div></div><div class="visual-bottom">CONNECT <i></i> SHARE <i></i> BELONG</div></div></div></section>
<div class="feature-strip"><div class="container"><span>One place. More ways to connect.</span><div>'''+icon('play')+''' Posts & videos</div><div>'''+icon('chat')+''' Conversations</div><div>'''+icon('people')+''' Communities</div></div></div>
<section class="section container" id="guides"><div class="section-top"><div><span class="eyebrow">FIND YOUR WAY</span><h2>A guide for every next step.</h2></div><p>From your first sign-in to your next community.<br>Start with what you want to do.</p></div><div class="guide-grid">'''+guide_cards()+'''</div></section>
<section class="overview-section"><div class="container overview-grid"><div><span class="eyebrow">MADE FOR EVERYDAY CONNECTION</span><h2>Your moments.<br>Your conversations.<br>Your community.</h2><p>Veepick brings content and conversation into the same experience. Explore the app at your own pace, then make it yours.</p><a class="text-link" href="https://veepick.com/">Visit Veepick '''+icon('arrow')+'''</a></div><div class="feature-list"><article><span>01</span><div><h3>Share what matters to you.</h3><p>Publish posts and videos, share stories, and join the conversation through comments and reactions.</p></div></article><article><span>02</span><div><h3>Keep in touch, your way.</h3><p>Start conversations, exchange media and use the call options available in your app.</p></div></article><article><span>03</span><div><h3>Build a space for your people.</h3><p>Explore groups and channels, follow updates and use the community controls available to your role.</p></div></article></div></div></section>
<section class="section container" id="help"><div class="help-grid"><div><span class="eyebrow">A LITTLE HELP GOES A LONG WAY</span><h2>Questions?<br>You’re in the right place.</h2><p>Find a quick answer, or get help with your app or account.</p><a class="text-link" href="mailto:support@veepick.com">Contact support '''+icon('mail')+'''</a></div><div class="faq"><details><summary>Where can I download Veepick?</summary><p>Use the <a href="https://veepick.com/download/">official Android download page</a> for the available download and installation information.</p></details><details><summary>What should I read first?</summary><p>Start with <a href="guides/getting-started.html">Getting started</a>. It covers installation, your account, your profile and finding your way around.</p></details><details><summary>Why do some options look different in my app?</summary><p>Features and labels may vary by app version, device, account and community permissions. Follow the controls shown in your installed version.</p></details><details><summary>How do I report an app problem?</summary><p>Use in-app support or email <a href="mailto:support@veepick.com">support@veepick.com</a>. Include your app version, device, what happened and the steps leading to it. Hide private information in screenshots.</p></details><details><summary>Can I suggest a change to these guides?</summary><p>Yes. <a href="https://github.com/raoofhassan0-web/Veepick-docs/issues">Open a documentation issue on GitHub</a> for an unclear explanation, a typo or a missing guide. Send account-specific requests directly to support.</p></details><details><summary>Does this repository include the app source code?</summary><p>This repository publishes Veepick’s public documentation and website. The application source repository is private.</p></details></div></div></section>
<section class="container download-panel"><div><span class="eyebrow">TAKE THE NEXT STEP</span><h2>Your world is waiting.</h2><p>Get Veepick for Android and make your next connection.</p></div><a class="button primary" href="https://veepick.com/download/">Download for Android '''+icon('download')+'''</a></section></main>'''
    return content+footer('')
def guide_html(guide):
    slug,num,title,desc,sections=guide
    prefix='../'
    side='<aside class="guide-sidebar"><a class="back-link" href="../index.html#guides">← All guides</a><div class="side-label">USER GUIDES</div><nav aria-label="User guides">'+''.join('<a href="'+g[0]+'.html"'+(' aria-current="page"' if g[0]==slug else '')+'>'+g[2]+'</a>' for g in GUIDES)+'</nav><div class="side-label toc-label">ON THIS PAGE</div><nav class="toc" aria-label="On this page">'+''.join('<a href="#step-'+str(i)+'">'+t+'</a>' for i,(t,p) in enumerate(sections,1))+'</nav></aside>'
    body='<main class="container guide-layout" id="main">'+side+'<article class="guide-article"><div class="breadcrumbs"><a href="../index.html">Docs</a><span>/</span><span>'+title+'</span></div><div class="eyebrow">GUIDE '+num+'</div><h1>'+title+'</h1><p class="guide-lead">'+desc+'</p><div class="guide-meta">Veepick user guide <span>·</span> Updated October 24, 2026</div><details class="mobile-contents"><summary>In this guide</summary><nav>'+''.join('<a href="#step-'+str(i)+'">'+t+'</a>' for i,(t,p) in enumerate(sections,1))+'</nav></details>'
    for i,(title_,text) in enumerate(sections,1):
        text=escape(text).replace('support@veepick.com','<a href="mailto:support@veepick.com">support@veepick.com</a>')
        if i==1 and slug=='getting-started':text+=' <a href="https://veepick.com/download/">Open Android downloads →</a>'
        body+='<section class="guide-section" id="step-'+str(i)+'"><h2><span>'+f'{i:02}'+'</span>'+title_+'</h2><p>'+text+'</p></section>'
    body+='<div class="guide-help"><strong>Need a hand?</strong><p>Contact <a href="mailto:support@veepick.com">support@veepick.com</a> for help with the app or your account.</p></div><div class="next-guides"><h2>Keep exploring</h2>'+''.join('<a href="'+g[0]+'.html">'+g[2]+icon('arrow')+'</a>' for g in GUIDES if g[0]!=slug)+'</div></article></main>'
    return head(title,desc,'guides/'+slug+'.html',prefix)+header(prefix,'guide')+body+footer(prefix)
def md_footer():
    return '\n---\n\n<p align="center">\n  <sub>© 2026 Veepick · <a href="https://veepick.com/terms/?lang=en">Terms</a> · <a href="https://veepick.com/community-guidelines/?lang=en">Community Guidelines</a> · <a href="https://veepick.com/child-safety/?lang=en">Child Safety</a> · <a href="https://veepick.com/delete-account/?lang=en">Account Deletion</a> · <a href="https://veepick.com/privacy/?lang=en">Privacy</a></sub>\n</p>\n'
def guide_md(guide):
    slug,num,title,desc,sections=guide
    return '[← Documentation home](../README.md)\n\n# '+title+'\n\n'+desc+'\n\n'+''.join('## '+str(i)+'. '+t+'\n\n'+p+'\n\n' for i,(t,p) in enumerate(sections,1))+'[Read this guide on the website]('+BASE+'guides/'+slug+'.html)\n'+md_footer()
README='''<p align="center">
  <img src="https://veepick.com/download/assets/veepick-icon.png" width="88" height="88" alt="Veepick" />
</p>

<h1 align="center">Veepick</h1>

<p align="center"><strong>Connect. Share. Find your community.</strong></p>
<p align="center">The official home of Veepick’s public guides and documentation.</p>

<p align="center">
  <a href="https://raoofhassan0-web.github.io/Veepick-docs/"><strong>Explore the documentation</strong></a>
  &nbsp; · &nbsp;
  <a href="https://veepick.com/download/">Get Veepick for Android</a>
  &nbsp; · &nbsp;
  <a href="https://veepick.com/">Website</a>
</p>

![Veepick — conversations, creativity and community](assets/docs-banner.svg)

## A place for your world

Veepick brings shared moments, everyday conversations and communities into one experience. This repository helps you find your way around the app and get more from the features available to you.

| Share your moments | Keep the conversation going | Find your people |
| --- | --- | --- |
| Posts, videos and stories, with comments and reactions. | Conversations, media sharing and available call options. | Groups and channels for discussions, updates and shared interests. |

## Start exploring

| Guide | What you’ll find |
| --- | --- |
| [Getting started](guides/getting-started.md) | Installation, your account, your profile and the first steps. |
| [Sharing & messaging](guides/sharing-and-messaging.md) | Posts, videos, upload progress, conversations and calls. |
| [Groups & channels](guides/communities.md) | Joining a community, roles, permissions and participation. |

Prefer a website? [Browse the complete documentation →](https://raoofhassan0-web.github.io/Veepick-docs/)

## Get Veepick

Visit the [official Android download page](https://veepick.com/download/) for the available download and installation information. Features and labels can vary by app version, device and account.

## Need a hand?

- **App or account help:** email [support@veepick.com](mailto:support@veepick.com), or use support inside Veepick.
- **A problem in these guides:** [open a documentation issue](https://github.com/raoofhassan0-web/Veepick-docs/issues) with the page and what needs to change.
- **A correction or improvement:** read the [contribution guide](CONTRIBUTING.md).

For an app issue, include the app version, device, steps and any visible error. Keep passwords, sign-in codes and private account information out of public GitHub issues. See [Support](SUPPORT.md) for more details.

## About this repository

This repository contains the public documentation and its GitHub Pages website. The Veepick application source repository is private. You can read the guides without an account or sign-in.
'''
SUPPORT='''# Support

Choose the right place for your request so it reaches the appropriate channel.

| Request | Where to go |
| --- | --- |
| App errors, sign-in problems or account questions | In-app support, or [support@veepick.com](mailto:support@veepick.com). |
| A report about content or an account | The Report option on the relevant content or account in Veepick. If unavailable, contact support. |
| An inaccurate explanation, typo or missing guide | [Documentation issues](https://github.com/raoofhassan0-web/Veepick-docs/issues). |
| An improvement to the documentation | Read [Contributing](CONTRIBUTING.md), then propose a focused change. |

## Help us understand an app problem

Include a short description, what you expected, what happened, the steps leading to it, your device, operating system and app version. If you include a screenshot, hide private information first.

Never send your password, sign-in codes or recovery credentials. GitHub issues are public; send account-specific requests directly to support.

## Reporting a security concern

Email [support@veepick.com](mailto:support@veepick.com?subject=Veepick%20security%20report) with “Security report” as the subject. Describe the affected feature, the impact and steps to reproduce the issue without exposing another person’s information. Keep vulnerability details out of public issues until they can be reviewed.

## About these guides

The guides describe the public user experience. Controls can vary with app updates, permissions and community roles. Follow the options shown in your installed version.
'''
CONTRIBUTING='''# Contributing to Veepick documentation

Thank you for helping make these guides clearer and more useful.

## Useful contributions

- Correct an inaccurate step or broken link.
- Clarify an explanation or fix a typo.
- Suggest a guide for a common task.
- Improve accessibility or the documentation layout.

## Before proposing a change

1. Check the existing guide and open documentation issues.
2. Describe the page, the problem and your proposed improvement in English.
3. Keep the change focused and use the labels shown in the app.
4. Do not include private conversations, account details or credentials.

Use [Support](SUPPORT.md) for app or account help.

## Editing the website and guides

The website uses static HTML and CSS. Its guide content and Markdown are generated together from `scripts/build_docs.py` using the Python standard library.

```sh
python3 scripts/build_docs.py
git diff --check
```

Edit guide content in the generator, regenerate the pages, and include the corresponding HTML and Markdown updates. Styling is maintained in `styles.css`. Preview the homepage and guide pages at desktop and mobile widths, and check navigation and keyboard focus before submitting a pull request.
'''

def build():
    files={'index.html':home(),'README.md':README+md_footer(),'SUPPORT.md':SUPPORT+md_footer(),'CONTRIBUTING.md':CONTRIBUTING+md_footer()}
    for g in GUIDES:
        files['guides/'+g[0]+'.html']=guide_html(g)
        files['guides/'+g[0]+'.md']=guide_md(g)
    for name,content in files.items():
        p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
        print(name)
if __name__=='__main__':build()
