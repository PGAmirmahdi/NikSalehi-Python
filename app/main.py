from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import date
from babel.dates import format_date
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
@app.get("/")
def root():
    return {"message": "FastAPI is running 🚀"}

def advertise():
    return [
        {
            "img_source":"/static/images/1.gif",
        },
        {
            "img_source": "/static/images/head-2.jpg",
        },
    ]
def ads():
    return [
        {
            "img_source":"/static/images/ad-1.jpg"
        },
        {
            "img_source": "/static/images/ad-2.jpg"
        },
        {
            "img_source": "/static/images/ad-3.jpg"
        },
        {
            "img_source": "/static/images/ad-4.jpg"
        }
    ]

def news():
    return [
        {
            "category":"مجله خبری",
            "title":"دختر موتورسوار باحجاب در راهپیمایی ۲۲ بهمن؛ نماد جدید مشارکت جوانان / فراسوی کلیشه‌ها",
            "img_source":"/static/images/1.jpg"
        },
        {
            "category": "آشپزی و دسر",
            "title": "دسرهای «بدون قند» با بافت جادویی: لذت شیرین بدون عذاب وجدان در سال ۲۰۲۶",
            "img_source": "/static/images/2.jpg"
        },
        {
            "category": "ورزشی",
            "title": "حمله بی‌پرده میثاقی به سروش رفیعی: وقتی حال نداری، برو بشین خانه! / درگیری کنایه پشت کنایه",
            "img_source": "/static/images/3.jpg"
        },
        {
            "category": "فال روزانه",
            "title": "فال روز چهارشنبه 22 بهمن ماه 1404",
            "img_source": "/static/images/4.jpg"
        },
        {
            "category": "گردشگری",
            "title": "جاده‌ای سفر کن و ایران را کشف کن؛ بهترین مسیرهای Road Trip ۱۴۰۵-۱۴۰۶ با ماشین شخصی یا ون + کمپینگ، موسیقی و منظره‌های نفس‌گیر که روحت رو تازه می‌کنه",
            "img_source": "/static/images/5.jpg"
        },
        {
            "category": "حوادث روز",
            "title": "تصاویر نقطه شروع آتش سوزی در بازارچه جنت / دوربین‌ها التهاب ۸ دقیقه‌ای ابتدای حادثه را فاش کردند",
            "img_source": "/static/images/6.jpg"
        },
    ]
def get_menu():
    return [
        {
            "title": "نیک صالحی",
            "url": "/niksalehi",
            "active": True,
            "children": []
        },
        {
            "title": "احکام",
            "url": "#",
            "active": False,
            "children": [
                {"title" : "استخاره با قرآن"},
            ]
        },
        {
            "title": "فال",
            "url": "#",
            "active": False,
            "children": [
                {"title": "فال و طالع بینی", "url": "#"},
                {"title": "فال روزانه", "url": "#"},
                {"title": "فال روز تولد", "url": "#"},
                {"title": "فال حافظ", "url": "#"},
                {"title": "فال کارت", "url": "#"},
                {"title": "فال چوب", "url": "#"},
                {"title": "فال شیخ بهایی", "url": "#"},
                {"title": "پیشگویی", "url": "#"},
            ]
        },
        {
            "title": "اخبار",
            "url": "#",
            "active": False,
            "children": [
                {"title": "اخبار ایران و جهان", "url": "#"},
                {"title": "اخبار اختصاصی", "url": "#"},
                {"title": "اخبار علمی", "url": "#"},
                {"title": "اخبار ورزشی", "url": "#"},
                {"title": "اخبار حوادث", "url": "#"},
                {"title": "موبایل و کامپیوتر", "url": "#"},
            ]
        },
        {
            "title": "سینما",
            "url": "#",
            "active": False,
            "children": [
                {"title": "فرهنگ و هنر", "url": "#"},
                {"title": "استوری چهره ها", "url": "#"},
                {"title": "فرهنگ و سینما", "url": "#"},
            ]
        },
        {
            "title": "سرگرمی",
            "url": "#",
            "active": False,
            "children": [
                {"title": "چه خبر از کجا؟", "url": "#"},
                {"title": "اس ام اس مناسبتی", "url": "#"},
                {"title": "مطالب گوناگون", "url": "#"},
                {"title": "سوژه های خنده دار", "url": "#"},
                {"title": "معما ،ضرب المثل ،چیستان", "url": "#"},
                {"title": "گزارش تصویری", "url": "#"},
                {"title": "داستان های کوتاه", "url": "#"},
                {"title": "خودرو", "url": "#"},
            ]
        },
        {
            "title": "گردشگری",
            "url": "#",
            "active": False,
            "children": []
        },
        {
            "title": "سلامت",
            "url": "#",
            "active": False,
            "children": [
                {"title": "شاخص توده بدنی", "url": "#"},
                {"title": "تغذیه و سلامت", "url": "#"},
                {"title": "پزشکی و درمان", "url": "#"},
                {"title": "زناشویی و همسرداری", "url": "#"},
                {"title": "آشپزی و دسر", "url": "#"},
                {"title": "روانشناسی", "url": "#"},
            ]
        },
        {
            "title": "سبک زندگی",
            "url": "#",
            "active": False,
            "children": [
                {"title": "مد روز", "url": "#"},
                {"title": "کاردستی", "url": "#"},
                {"title": "زیبایی و آرایش", "url": "#"},
                {"title": "خانه داری", "url": "#"},
                {"title": "دکوراسیون", "url": "#"},
            ]
        },
        {
            "title": "ویدیو",
            "url": "#",
            "active": False,
            "children": []
        },
    ]
def today_fa():
    today = date.today()
    return format_date(
        today,
        format="EEEE, d MMMM , y",
        locale="fa_IR"
    )
@app.get("/niksalehi", response_class=HTMLResponse)
def niksalehi(request: Request):
    return templates.TemplateResponse(
        "niksalehi.html",
        {
            "request": request,
            "title": "نیک صالحی",
            "menu": get_menu(),
            "today": today_fa(),
            "advertise": advertise(),
            "news": news(),
            "ads": ads(),
        }
    )