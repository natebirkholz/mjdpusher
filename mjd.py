import json
import requests

url = 'https://careers.mjdinteractive.com/application'
intro = ''' I have been working as an iOS developer for two and half years. Prior to that I was 
an iOS programming student, and before that I had a long career as a video game producer. I 
eventually rose in my career to the point where I just talked about doing work all day instead 
of actually `doing` work, so I decided on a career change. For years I had been learning 
programming and architecture from coworkers and from meetings and interviewing candidates and 
I had dabbled in C and Python. I had also grown up programming as a teenager, so a career change 
to programming was an exciting but natural step, especially after a couple colleagues recommended
that I try it based in my technical aptitude. I've been working as a programmer full time (and 
more) for the past two years and a reduction in force at my last job put me somewhat unexpectedly 
on the job market. 
I enjoyed the test and look forward to your feedback. I added some comments to the `Readme.md` 
file in the repo for your information. For next steps, I would likely get the detail view 
controller working and populated with the details of the cat selected from the `UITableview` and
then I would get the `KittyCell` caption to be sized to fit the text, which would also require
the cell itself to size dynamically to fit the number of lines if they exceeeded two. I'd figure 
out why one of the cat images is failing to initialize from the web fetch (Clyde's image). I'd 
then fix the bug with the divider lines not appearing between the cells in the tableView. I'd 
next research ways to make the `Cat` model to be a struct again. I'd also coax the 
`CatListingTableViewController` into letting me rename `tableVIew` to `tableView`, last time I 
had to do that it was a major pain, always good to have a reason to avoid typos! 
I look forward to hearing from you. I'm truly intrigued by MJD and hope to get a chance to 
learn more!'''

jsonData = {'firstName': 'Nate','lastName': 'Birkholz','email': 'nbirkholz@gmail.com','phone': '612-247-7126','address': '1427 1/2 B Fern St, San Diego, CA 92102','projectRepo': 'https://github.com/natebirkholz/KittenKompare','resumeURL': 'https://docs.google.com/document/d/1Q4Sv1OWHidvNxFpgodgHxEO8pMMzgkESApYrmo3WqLE/edit?usp=sharing','position': 'Senior iOS Engineer','introduction': intro}
r = requests.post(url, json=jsonData)

print(r.status_code)