from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from werkzeug.utils import secure_filename
from datetime import datetime
import time
import json
import os


# -- OPEN JSON FILE ---
with open("config.json", "r") as f:
    params = json.load(f)["params"]


Time = time.asctime(time.localtime(time.time()))


# --- APP CONFIG & DB CONNECTION ---
local_server = True
app = Flask(__name__)
app.secret_key = 'the-random-string'
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config['PORT_UPLOAD_FOLDER'] = params['port_upload_location']
app.config['TESTI_UPLOAD_FOLDER'] = params['testi_upload_location']


if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


# ---- DB TABLE CONFIG ------
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)

class Credentials(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

class About(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    about_head = db.Column(db.String(300), nullable=False)
    heading = db.Column(db.String(20), nullable=False)
    about_details = db.Column(db.String(500), nullable=False)

class Portfolio(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    portfolio_head = db.Column(db.String(500), nullable=False)

class Apps(db.Model): 
    sno = db.Column(db.Integer, primary_key=True)
    app_img = db.Column(db.String(20), nullable=False)
    app_url = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    app_title = db.Column(db.String(100), nullable=False)
    app_content = db.Column(db.String(1000), nullable=False)
    app_client = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(12), nullable=False)

class Card(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    card_img = db.Column(db.String(20), nullable=False)
    card_url = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    card_title = db.Column(db.String(100), nullable=False)
    card_content = db.Column(db.String(1000), nullable=False)
    card_client = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(12), nullable=False)

class Web(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    web_img = db.Column(db.String(20), nullable=False)
    web_url = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    web_title = db.Column(db.String(100), nullable=False)
    web_content = db.Column(db.String(1000), nullable=False)
    web_client = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    

class Profile(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    send_mail = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    location_url = db.Column(db.String(100), nullable=False)
    location_map = db.Column(db.String(100), nullable=False)
    phone_num = db.Column(db.String(20), nullable=False)
    call_url = db.Column(db.String(20), nullable=False)
    website = db.Column(db.String(20), nullable=False)
    pro_img = db.Column(db.String(20), nullable=False)
    bg_img = db.Column(db.String(20), nullable=False)

class Social(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    github = db.Column(db.String(20), nullable=False)
    youtube = db.Column(db.String(20), nullable=False)
    twitter = db.Column(db.String(20), nullable=False)
    instagram = db.Column(db.String(20), nullable=False)
    linkedin = db.Column(db.String(20), nullable=False)

class Skills(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    skills_data = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(20), nullable=False)

class Skillhead(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    head = db.Column(db.String(1000), nullable=False)

class Resume(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    resume_head = db.Column(db.String(1000), nullable=False)

class Resumesummary(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(1000), nullable=False)

class Education(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(20), nullable=False)
    institute = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

class Proex(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(100), nullable=False) 
    year = db.Column(db.String(20), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

class Facts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(20), nullable=False) 
    fact = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)

class Facthead(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    fact_head = db.Column(db.String(1000), nullable=False)

class Servicehead(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    head = db.Column(db.String(200), nullable=False)

class Services(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(20), nullable=False) 
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)

class Thead(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    head = db.Column(db.String(1000), nullable=False)

class Testimonials(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False) 
    email = db.Column(db.String(50), nullable=False) 
    occupation = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    img = db.Column(db.String(50), nullable=False)

# --- CONNECTING MAIL SERVER -----
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password']
)
mail = Mail(app)


# ----------- HOME PAGE ---------------- 
@app.route("/", methods=['GET', 'POST'])
def home():
    # ------ TABLE CONFIG --------
    about = About.query.filter_by(sno=1).first()
    social = Social.query.filter_by(sno=1).first()
    profile = Profile.query.filter_by(sno=1).first()
    resume = Resume.query.filter_by(sno=1).first()
    resumesummary = Resumesummary.query.filter_by(sno=1).first()
    skillhead = Skillhead.query.filter_by(sno=1).first()
    portfolio = Portfolio.query.filter_by(sno=1).first()
    facthead = Facthead.query.filter_by(sno=1).first()
    servicehead = Servicehead.query.filter_by(sno=1).first()
    thead = Thead.query.filter_by(sno=1).first()
    education = Education.query.filter_by().all()
    proex = Proex.query.filter_by().all()
    skills = Skills.query.filter_by().all()
    apps = Apps.query.filter_by().all()
    card = Card.query.filter_by().all()
    web = Web.query.filter_by().all()
    facts = Facts.query.filter_by().all()
    services = Services.query.filter_by().all()
    testimonials = Testimonials.query.filter_by().all()

    if (request.method=='POST'):
        """ ADD ENTRY TO DATABASE """

        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        #---- ADD DATA IN THE DATABASE ---- 
        entry = Contacts(name=name, subject=subject, email=email, date=Time)
        db.session.add(entry)
        db.session.commit()

        #---- SENDING MAIL ---
        mail.send_message(
            subject= subject,
            sender = email,
            body = f"Name:-  {name} \nEmail:-  {email} \n{message} " ,
            recipients = [params['gmail_user']]
        )
        flash("Sent", "success")

    
    return render_template("index.html", params=params, about=about, portfolio=portfolio, profile=profile, social=social, 
    skills=skills, skillhead=skillhead, apps=apps, card=card, web=web, resume=resume, resumesummary=resumesummary, 
    education=education, proex=proex, facts=facts, facthead=facthead, servicehead=servicehead, services=services, 
    thead=thead, testimonials=testimonials)

# ----------------- COMMENT PAGE ------------
@app.route("/comment", methods=['GET', 'POST'])
def comment():
    if (request.method=='POST'):
        """ ADD ENTRY TO COMMENTS """

        tname = request.form.get('tname')
        temail = request.form.get('temail')
        occupation = request.form.get('occupation')
        picture = request.form.get('picture')
        comment = request.form.get('comment')

        add = Testimonials(name=tname, email=temail, occupation=occupation, img=picture, comment=comment)
        db.session.add(add)
        db.session.commit()
        flash("Submited", "success")


    social = Social.query.filter_by(sno=1).first()
    profile = Profile.query.filter_by(sno=1).first()
    return render_template("comment.html", params=params, profile=profile, social=social) 


# --------------- PORTFOLIO-DETAILS PAGE ------------------------ 
@app.route("/portfolio-apps/<string:apps_slug>", methods=['GET'])
def portfolio_apps(apps_slug):
    portfolio_apps = Apps.query.filter_by(slug=apps_slug).first()
    social = Social.query.filter_by(sno=1).first()
    profile = Profile.query.filter_by(sno=1).first()

    return render_template("portfolio-apps.html", params=params, profile=profile, social=social, portfolio_apps=portfolio_apps)

@app.route("/portfolio-card/<string:card_slug>", methods=['GET'])
def portfolio_card(card_slug):
    portfolio_card = Card.query.filter_by(slug=card_slug).first()
    social = Social.query.filter_by(sno=1).first()
    profile = Profile.query.filter_by(sno=1).first()

    return render_template("portfolio-card.html", params=params, profile=profile, social=social, portfolio_card=portfolio_card)

@app.route("/portfolio-web/<string:web_slug>", methods=['GET'])
def portfolio_web(web_slug):
    portfolio_web = Web.query.filter_by(slug=web_slug).first()
    social = Social.query.filter_by(sno=1).first()
    profile = Profile.query.filter_by(sno=1).first()

    return render_template("portfolio-web.html", params=params, profile=profile, social=social, portfolio_web=portfolio_web)
# --------------- PORTFOLIO-DETAILS PAGE END ------------------------ 

# ------ LOGIN & DASHBORD PAGE -------------
@app.route("/dashboard", methods=['GET', 'POST'])
def login():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()
    
    if ('user' in session and session['user'] == admin_user ):
        return render_template("dashboard.html", params=params, profile=profile)

    if request.method == 'POST':
        # ---- REDIRECT TO ADMIN PANEL -----
        username = request.form.get('uname')
        userpass = request.form.get('pass')

        # --------- VERIFY THE USERNAME & PASSWORD ------
        if (username == admin_user and userpass == admin_password ):
            
            # ----- SET THE SESSION VARIABLE ----
            session['user'] = username
            return render_template("dashboard.html", params=params, profile=profile)
        else:
            flash("Wrong username or password", "danger")

    return render_template("login.html")
# ------ LOGIN & DASHBORD PAGE END -------------


# --------- ABOUT UPDATE ---------------
@app.route("/about-update", methods=['GET', 'POST'])
def about_update():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user ):

        if (request.method=='POST'):
            about = About.query.filter_by(sno=1).first()
            about.about_head = request.form.get('about_head')
            about.heading = request.form.get('about_heading')
            about.about_details= request.form.get('about_details')
            db.session.commit()
            flash("Updated", "success")
            return redirect("/about-update")        
    
    else:
        return redirect("/dashboard")

    about = About.query.filter_by(sno=1).first()
    return render_template("about-update.html", params=params, profile=profile, about=about)
# --------- ABOUT UPDATE END ---------------


# --------- RESUME UPDATE ----------------------------------------
@app.route("/resume-update", methods=['GET', 'POST'])
def resume_update():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user ):

        if (request.method=='POST'):
            resume = Resume.query.filter_by(sno=1).first()
            resumesummary = Resumesummary.query.filter_by(sno=1).first()

            resume.resume_head = request.form.get('resume_head')
            resumesummary.summary = request.form.get('summary')

            db.session.commit()
            flash("Updated", "success")
            return redirect("/resume-update")

    else:
        return redirect("/dashboard")

    proex = Proex.query.filter_by().all()
    education = Education.query.filter_by().all()
    resume = Resume.query.filter_by(sno=1).first()
    resumesummary = Resumesummary.query.filter_by(sno=1).first()
    return render_template("resume-update.html", params=params, profile=profile, resume=resume, resumesummary=resumesummary, education=education, proex=proex)


# ------ EDUCATION EDIT PAGE -----------------------------
@app.route("/edu-edit/<string:sno>", methods=['GET', 'POST'])
def edu_edit(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user ):

        if request.method == 'POST':
            course = request.form.get('course')
            year = request.form.get('year')
            institute = request.form.get('institute')
            description = request.form.get('description')

            if sno == "0":
                education = Education(course=course, year=year, institute=institute, description=description)
                db.session.add(education)
                db.session.commit()
                flash("Added", "success")
                
            else:
                education = Education.query.filter_by(sno=sno).first()
                education.course = course
                education.year = year
                education.institute = institute
                education.description = description
                db.session.commit()
                flash("Updated", "success")
                return redirect("/edu-edit/" + sno)
    else:
        return redirect("/dashboard")

    education = Education.query.filter_by(sno=sno).first()         
    return render_template("edu-edit.html", params=params, profile=profile, education=education, sno=sno)


# ----- EDUCATION DELETE ------------
@app.route("/edu-delete/<string:sno>", methods=['GET', 'POST'])
def edu_delete(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):
        education = Education.query.filter_by(sno=sno).first()
        db.session.delete(education)
        db.session.commit()
        flash("Deleted", "danger")
        return redirect("/resume-update")
    
    else:
        return redirect("/dashboard")


# ------ PROEX EDIT --------------------------
@app.route("/pro-edit/<string:sno>", methods=['GET', 'POST'])
def pro_edit(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user):

        if request.method == 'POST':
            course = request.form.get('course')
            year = request.form.get('year')
            company = request.form.get('company')
            description = request.form.get('description')

            if sno == "0":
                proex = Proex(course=course, year=year, company=company, description=description)
                db.session.add(proex)
                db.session.commit()
                flash("Added", "success")

            else:
                proex = Proex.query.filter_by(sno=sno).first()
                proex.course = course
                proex.year = year
                proex.company = company
                proex.description = description
                db.session.commit()
                flash("Updated", "success")
                return redirect("/pro-edit/" + sno)
    else:
        return redirect("/dashboard")

    proex = Proex.query.filter_by(sno=sno).first()            
    return render_template("pro-edit.html", params=params, profile=profile, proex=proex, sno=sno)


# ----- PROEX DELETE ------------
@app.route("/pro-delete/<string:sno>", methods=['GET', 'POST'])
def pro_delete(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):
        proex = Proex.query.filter_by(sno=sno).first()
        db.session.delete(proex)
        db.session.commit()
        flash("Deleted", "danger")
        return redirect("/resume-update")
    
    else:
        return redirect("/dashboard")
# --------- RESUME UPDATE END -----------------------------


# --------- PORTFOLIO UPDATE --------------------
@app.route("/portfolio-update", methods=['GET', 'POST'])
def portfolio_update():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user ):
        
        if request.method == 'POST':
            portfolio = Portfolio.query.filter_by(sno=1).first()
            portfolio.portfolio_head = request.form.get('portfolio_head')
            db.session.commit()
            flash("Updated", "success")
            return redirect("/portfolio-update")

    else:
        return redirect("/dashboard")

    apps = Apps.query.filter_by().all()
    card = Card.query.filter_by().all()
    web = Web.query.filter_by().all()
    portfolio = Portfolio.query.filter_by(sno=1).first()
    return render_template("portfolio-update.html", params=params, profile=profile, portfolio=portfolio, apps=apps, card=card, web=web)


# ------ APPS EDIT -----------
@app.route("/apps-edit/<string:sno>", methods=['GET', 'POST'])
def apps_edit(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user):

        if request.method == 'POST':
            image = request.form.get('image')
            url = request.form.get('url')
            slug = request.form.get('slug')
            title = request.form.get('title')
            client = request.form.get('client')
            content = request.form.get('content')

            if sno == "0":
                apps = Apps(app_img=image, app_url=url, slug=slug, app_title=title, app_content=content,  app_client=client,date=datetime.now())
                db.session.add(apps)
                db.session.commit()
                flash("Added", "success")

            else:
                apps = Apps.query.filter_by(sno=sno).first()
                apps.app_img = image
                apps.app_url = url
                apps.slug = slug
                apps.app_title = title
                apps.app_content = content
                apps.app_client = client
                apps.date = datetime.now()
                db.session.commit()
                flash("Updated", "success")
                return redirect("/apps-edit/" + sno)
    else:
        return redirect("/dashboard")

    apps = Apps.query.filter_by(sno=sno).first()            
    return render_template("apps-edit.html", params=params, profile=profile, apps=apps, sno=sno)


# ----- APPS DELETE ------------
@app.route("/apps-delete/<string:sno>", methods=['GET', 'POST'])
def apps_delete(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):
        apps = Apps.query.filter_by(sno=sno).first()
        db.session.delete(apps)
        db.session.commit()
        flash("Deleted", "danger")
        return redirect("/portfolio-update")
    
    else:
        return redirect("/dashboard")


# ------ CARD EDIT -----------
@app.route("/card-edit/<string:sno>", methods=['GET', 'POST'])
def card_edit(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user):

        if request.method == 'POST':
            image = request.form.get('image')
            url = request.form.get('url')
            slug = request.form.get('slug')
            title = request.form.get('title')
            client = request.form.get('client')
            content = request.form.get('content')

            if sno == "0":
                card = Card(card_img=image, card_url=url, slug=slug, card_title=title, card_content=content, card_client=client,date=datetime.now())
                db.session.add(card)
                db.session.commit()
                flash("Added", "success")

            else:
                card = Card.query.filter_by(sno=sno).first()
                card.card_img = image
                card.card_url = url
                card.slug = slug
                card.card_title = title
                card.card_content = content
                card.card_client = client
                card.date = datetime.now()
                db.session.commit()
                flash("Updated", "success")
                return redirect("/card-edit/" + sno)
    else:
        return redirect("/dashboard")

    card = Card.query.filter_by(sno=sno).first()            
    return render_template("card-edit.html", params=params, profile=profile, card=card, sno=sno)


# ----- CARD DELETE ------------
@app.route("/card-delete/<string:sno>", methods=['GET', 'POST'])
def card_delete(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):
        card = Card.query.filter_by(sno=sno).first()
        db.session.delete(card)
        db.session.commit()
        flash("Deleted", "danger")
        return redirect("/portfolio-update")
    
    else:
        return redirect("/dashboard")


# ------ WEB EDIT -----------
@app.route("/web-edit/<string:sno>", methods=['GET', 'POST'])
def web_edit(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user):

        if request.method == 'POST':
            image = request.form.get('image')
            url = request.form.get('url')
            slug = request.form.get('slug')
            title = request.form.get('title')
            client = request.form.get('client')
            content = request.form.get('content')

            if sno == "0":
                web = Web(web_img=image, web_url=url, slug=slug, web_title=title, web_content=content, web_client=client,date=datetime.now())
                db.session.add(web)
                db.session.commit()
                flash("Added", "success")

            else:
                web = Web.query.filter_by(sno=sno).first()
                web.web_img = image
                web.web_url = url
                web.slug = slug
                web.web_title = title
                web.web_content = content
                web.web_client = client
                web.date = datetime.now()
                db.session.commit()
                flash("Updated", "success")
                return redirect("/web-edit/" + sno)
    else:
        return redirect("/dashboard")

    web = Web.query.filter_by(sno=sno).first()            
    return render_template("web-edit.html", params=params, profile=profile, web=web, sno=sno)


# ----- WEB DELETE ------------
@app.route("/web-delete/<string:sno>", methods=['GET', 'POST'])
def web_delete(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):
        web = Web.query.filter_by(sno=sno).first()
        db.session.delete(web)
        db.session.commit()
        flash("Dedleted", "danger")
        return redirect("/portfolio-update")
    
    else:
        return redirect("/dashboard")


# ------- UPLOAD PORTFOLIO IMAGE ----------------
@app.route("/port-uploader", methods=['GET', 'POST'])
def port_uploader():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user ):

        if request.method == 'POST':
            f = request.files['filename']
            f.save(os.path.join(app.config['PORT_UPLOAD_FOLDER'], secure_filename(f.filename)))
            flash("Submited", "success")
            return redirect("/portfolio-update")
    else:
        return redirect("/dashboard")
# --------- PORTFOLIO UPDATE END -----------------------

# --------- FACT UPDATE -------------------------
@app.route("/facts-update", methods=['GET', 'POST'])
def facts_update():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user ):
        
        if request.method == 'POST':
            facthead = Facthead.query.filter_by(sno=1).first()

            facthead.fact_head = request.form.get('facthead')
            db.session.commit()
            flash("Updated", "success")
            return redirect("/facts-update")

        
    else:
        return redirect("/dashboard")

    profile = Profile.query.filter_by(sno=1).first()
    facthead = Facthead.query.filter_by(sno=1).first()
    facts = Facts.query.filter_by().all()
    return render_template("facts-update.html", params=params, profile=profile, facthead=facthead, facts=facts)


# ------ FACTS EDIT -----------
@app.route("/facts-edit/<string:sno>", methods=['GET', 'POST'])
def facts_edit(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):

        if request.method == 'POST':
            icon = request.form.get('icon')
            fact = request.form.get('fact')
            title = request.form.get('title')
            description = request.form.get('description')

            if sno == "0":
                facts = Facts(icon=icon, fact=fact, title=title, description=description)
                db.session.add(facts)
                db.session.commit()
                flash("Added", "success")

            else:
                facts = Facts.query.filter_by(sno=sno).first()
                facts.icon = icon
                facts.fact = fact
                facts.title = title
                facts.description = description
                
                db.session.commit()
                flash("Updated", "success")
                return redirect("/facts-edit/" + sno)
    else:
        return redirect("/dashboard")

    profile = Profile.query.filter_by(sno=1).first() 
    facts = Facts.query.filter_by(sno=sno).first()       
    return render_template("facts-edit.html", params=params, profile=profile, sno=sno, facts=facts)


# ----- FACTS DELETE ------------
@app.route("/facts-delete/<string:sno>", methods=['GET', 'POST'])
def facts_delete(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):
        facts = Facts.query.filter_by(sno=sno).first()
        db.session.delete(facts)
        db.session.commit()
        flash("Deleted", "danger")
        return redirect("/facts-update")
    
    else:
        return redirect("/dashboard")
# --------- FACT UPDATE END -------------------------



# ----------------- TESTIMONIALS UPDATE -------------------
@app.route("/testimonials-update", methods=['GET', 'POST'])
def testimonials_update():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user ):
        
        if request.method == 'POST':
            thead = Thead.query.filter_by(sno=1).first()

            thead.head= request.form.get('head')
            db.session.commit()
            flash("Updated", "success")
            return redirect("/testimonials-update")

        
    else:
        return redirect("/dashboard")

    profile = Profile.query.filter_by(sno=1).first()
    thead = Thead.query.filter_by(sno=1).first()
    testimonials = Testimonials.query.filter_by().all()
    return render_template("testimonials-update.html", params=params, profile=profile, thead=thead, testimonials=testimonials)


# ----- TESTIMONIALS DELETE ------------
@app.route("/testimonials-delete/<string:sno>", methods=['GET', 'POST'])
def testimonials_delete(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):
        testimonials = Testimonials.query.filter_by(sno=sno).first()
        db.session.delete(testimonials)
        db.session.commit()
        flash("Deleted", "danger")
        return redirect("/testimonials-update")
    
    else:
        return redirect("/dashboard")

# ------- UPLOAD TESTIMONIALS IMAGES ----------------
@app.route("/testimonials-uploader", methods=['GET', 'POST'])
def testimonials_uploader():
        if request.method == 'POST':
            f = request.files['filename']
            f.save(os.path.join(app.config['TESTI_UPLOAD_FOLDER'], secure_filename(f.filename)))
            flash("Submited", "success")
            return redirect("/comment")

# ----------------- TESTIMONIALS UPDATE END ---------------


# --------- SKILLS UPDATE ---------------
@app.route("/skills-update", methods=['GET', 'POST'])
def skills_update():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user ):
        
        if request.method == 'POST':
            skillhead = Skillhead.query.filter_by(sno=1).first()
            skillhead.head = request.form.get('head')
            db.session.commit()
            flash("Updated", "success")
            return redirect("/skills-update")
        
    else:
        return redirect("/dashboard")

    skills = Skills.query.filter_by().all()
    skillhead = Skillhead.query.filter_by(sno=1).first()
    profile = Profile.query.filter_by(sno=1).first() 
    return render_template("skills-update.html", params=params, profile=profile, skillhead=skillhead, skills=skills)


# ------ SKILLS EDIT -----------
@app.route("/skills-edit/<string:sno>", methods=['GET', 'POST'])
def skills_edit(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):

        if request.method == 'POST':
            skills_data = request.form.get('skills_data')
            level = request.form.get('level')
            

            if sno == "0":
                skills = Skills(skills_data=skills_data, level=level)
                db.session.add(skills)
                db.session.commit()
                flash("Added", "success")

            else:
                skills = Skills.query.filter_by(sno=sno).first()
                skills.skills_data = skills_data
                skills.level = level
                
                db.session.commit()
                flash("Updated", "success")
                return redirect("/skills-edit/" + sno)
    else:
        return redirect("/dashboard")
 
    skills = Skills.query.filter_by(sno=sno).first()
    profile = Profile.query.filter_by(sno=1).first()      
    return render_template("skills-edit.html", params=params, profile=profile, sno=sno, skills=skills)


# ----- SKILLS DELETE ------------
@app.route("/skills-delete/<string:sno>", methods=['GET', 'POST'])
def skills_elete(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):
        skills = Skills.query.filter_by(sno=sno).first()
        db.session.delete(skills)
        db.session.commit()
        flash("Deleted", "danger")
        return redirect("/skills-update")
    
    else:
        return redirect("/dashboard")

# -------------- SKILLS UPDATE END --------------------------------


# ---------  SERVICE UPDATE ---------------
@app.route("/services-update", methods=['GET', 'POST'])
def services_update():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user ):
        
        if request.method == 'POST':
            servicehead = Servicehead.query.filter_by(sno=1).first()
            servicehead.head = request.form.get('head')
            db.session.commit()
            flash("Updated", "success")
            return redirect("/services-update")
        
    else:
        return redirect("/dashboard")

    services = Services.query.filter_by().all()
    servicehead = Servicehead.query.filter_by(sno=1).first()
    profile = Profile.query.filter_by(sno=1).first()
    return render_template("services-update.html", params=params, profile=profile, services=services, servicehead=servicehead)

# ------ SERVICES EDIT -----------
@app.route("/services-edit/<string:sno>", methods=['GET', 'POST'])
def services_edit(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):

        if request.method == 'POST':
            icon = request.form.get('icon')
            title = request.form.get('title')
            description = request.form.get('description')
            link = request.form.get('link')
            
            if sno == "0":
                services = Services(icon=icon, title=title, description=description, link=link)
                db.session.add(services)
                db.session.commit()
                flash("Added", "success")

            else:
                services = Services.query.filter_by(sno=sno).first()
                services.icon = icon
                services.title = title
                services.description = description
                services.link = link
                
                db.session.commit()
                flash("Updated", "success")
                return redirect("/services-edit/" + sno)
    else:
        return redirect("/dashboard")
 
    services = Services.query.filter_by(sno=sno).first()
    profile = Profile.query.filter_by(sno=1).first()      
    return render_template("services-edit.html", params=params, profile=profile, sno=sno, services=services)


# ----- SKILLS DELETE ------------
@app.route("/services-delete/<string:sno>", methods=['GET', 'POST'])
def services_elete(sno):
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user):
        services = Services.query.filter_by(sno=sno).first()
        db.session.delete(services)
        db.session.commit()
        flash("Deleted", "danger")
        return redirect("/services-update")
    
    else:
        return redirect("/dashboard")


# ---------  SERVICE UPDATE END---------------

# --------- SOCIAL UPDATE ---------------
@app.route("/social-update", methods=['GET', 'POST'])
def social_update():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user ):

        if (request.method=='POST'):
            social = Social.query.filter_by(sno=1).first()

            social.github = request.form.get('git_url')
            social.youtube = request.form.get('yt_url')
            social.twitter= request.form.get('twt_url')
            social.instagram= request.form.get('insta_url')
            social.linkedin= request.form.get('link_url')

            db.session.commit()
            flash("Updated", "success")

            return redirect("/social-update") 

    else:
        return redirect("/dashboard")

    social = Social.query.filter_by(sno=1).first()
    return render_template("social-update.html", params=params, profile=profile, social=social)
# --------- SOCIAL UPDATE END ---------------


# --------- PROFILE UPDATE ---------------
@app.route("/profile-update", methods=['GET', 'POST'])
def profile_update():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user ):

        if (request.method=='POST'):
            profile = Profile.query.filter_by(sno=1).first()

            profile.name = request.form.get('name')
            profile.dob = request.form.get('dob')
            profile.email= request.form.get('email')
            profile.send_mail= request.form.get('send_mail')
            profile.location= request.form.get('location')
            profile.location_url= request.form.get('location_url')
            profile.location_map= request.form.get('location_map')
            profile.phone_num= request.form.get('phone_num')
            profile.call_url= request.form.get('call_url')
            profile.website= request.form.get('website')
            profile.pro_img= request.form.get('pro_img')
            profile.bg_img= request.form.get('bg_img')

            db.session.commit()
            flash("Updated", "success")
            return redirect("/profile-update")

    else:
        return redirect("/dashboard")
    return render_template("profile-update.html", params=params, profile=profile)


# ------- UPLOAD PROFILE AND BG IMAGE ----------------
@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password

    if ('user' in session and session['user'] == admin_user ):

        if request.method == 'POST':
            f = request.files['filename']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            flash("Submited", "success")
            return redirect("/profile-update")
    else:
        return redirect("/dashboard")
# --------- PROFILE UPDATE END --------------------------


# --------- PASSWORD UPDATE -------------------------------
@app.route("/password-update", methods=['GET', 'POST'])
def password_update():
    # --------- LOGIN CONFIG -------
    loginkey = Credentials.query.filter_by(sno=1).first()
    admin_user = loginkey.username
    admin_password = loginkey.password
    
    profile = Profile.query.filter_by(sno=1).first()

    if ('user' in session and session['user'] == admin_user ):

        if (request.method=='POST'):
            credentials = Credentials.query.filter_by(sno=1).first()

            credentials.username = request.form.get('uname')
            credentials.password = request.form.get('pass')
            credentials.email = request.form.get('email')

            db.session.commit()
            flash("Updated", "success")
            return redirect("/password-update")

    else:
        return redirect("/dashboard")

    
    return render_template("password-update.html", params=params, profile=profile, loginkey=loginkey)
# --------- PASSWORD UPDATE END -------------------------------

# ----- LOGOUT -----------
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)