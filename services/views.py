from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Service, Venue

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        # 🔐 Add authentication logic here (username/password)
        
        # ✅ After successful login → redirect to Services section
        return redirect('/#services')

    return render(request, 'login.html')

# Render wedding page
def wedding_page(request):
    return render(request, "wedding.html")

# Render venue page
def venue_page(request):
    return render(request, "venue.html")

def venue1_page(request):
    return render(request, "venue1.html")

# API: Get all services
def get_services(request):
    services = list(Service.objects.values())
    return JsonResponse(services, safe=False)

# API: Get all venues
def get_venue(request):
    venues = list(Venue.objects.values())
    return JsonResponse(venues, safe=False)

# API: Add a new venue
@csrf_exempt
def add_venue(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Venue.objects.create(
            name=data.get("name"),
            location=data.get("location"),
            price=data.get("price"),
            rating=data.get("rating", 4)
        )
        return JsonResponse({"message": "Venue added successfully"})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower()

        # Greetings
        if "hello" in user_message or "hi" in user_message:
            bot_reply = "Hello! Welcome to Evento. How can I help you today?"

        # About Evento
        elif "what is evento" in user_message or "about evento" in user_message:
            bot_reply = "Evento is an online event management platform to plan weddings, birthdays, receptions, and corporate events easily."

        # Account
        elif "create account" in user_message or "register" in user_message:
            bot_reply = "To create an account, click on Login/Register, enter your email, phone number, and set a password."

        elif "login" in user_message:
            bot_reply = "Use your registered email and password on the login page to access your Evento account."

        # Events
        elif "event" in user_message or "types of events" in user_message or "available events" in user_message:
            bot_reply = "We organize weddings, birthdays, receptions, engagements, anniversaries, and corporate events."

        # Booking
        elif "how to book" in user_message or "booking process" in user_message or "booking" in user_message:
            bot_reply = (
                "Booking steps:\n"
                "1. Choose event type\n"
                "2. Select services\n"
                "3. Choose venue\n"
                "4. Pick date & time\n"
                "5. Confirm booking\n"
                "6. Make payment"
            )

        # Pricing
        elif "price" in user_message or "cost" in user_message:
            bot_reply = "Pricing depends on event type and selected services. Please specify your event."

        # Wedding / Marriage
        elif "marriage" in user_message or "wedding" in user_message:
            bot_reply = "Our wedding packages include decoration, catering, photography, and entertainment."

        # Birthday
        elif "birthday" in user_message:
            bot_reply = "Birthday packages include themes, cakes, games, decorations, and entertainment."

        # Reception
        elif "reception" in user_message:
            bot_reply = "Reception events can be customized with seating, lighting, and music."

        # Services
        elif "services" in user_message or "offer" in user_message:
            bot_reply = "We offer catering, decoration, entertainment, photography, venue booking, and complete event planning."

        elif "catering" in user_message:
            bot_reply = "We provide veg, non-veg, buffet, traditional, and customized catering services."

        elif "decoration" in user_message:
            bot_reply = "Decoration includes flowers, stage setup, lighting, and theme-based designs."

        elif "photography" in user_message or "videography" in user_message or "photo" in user_message:
            bot_reply = "Professional photography and videography services are available."

        elif "entertainment" in user_message:
            bot_reply = "We arrange DJs, live music, games, and performances."

        # Customization
        elif "customize" in user_message or "customization" in user_message:
            bot_reply = "Yes, all event packages can be customized based on your requirements and budget."

        # Guest Capacity
        elif "guest" in user_message or "capacity" in user_message:
            bot_reply = "We handle events from small gatherings up to 500+ guests."

        # Venues
        elif "top 5 venues" in user_message:
            bot_reply = (
                "Top 5 venues in Evento:\n"
                "1. Thirumalai Mahal\n"
                "2. Kaveri Palace\n"
                "3. Royal Wedding Hall\n"
                "4. Grand Convention Center\n"
                "5. Green Valley Resort"
            )

        elif "best venue" in user_message or "recommended venue" in user_message:
            bot_reply = "Thirumalai Mahal is our most recommended venue for weddings and receptions."

        elif "under 30000" in user_message or "budget venue" in user_message or "low cost venue" in user_message:
            bot_reply = (
                "Venues available under ₹30,000:\n"
                "1. Thirumalai Mini Hall\n"
                "2. Kaveri Community Hall\n"
                "3. SV Mahal\n"
                "4. Arj Party Hall\n"
                "5. Local Community Mandapam"
            )

        elif "venue" in user_message or "location" in user_message:
            bot_reply = "We can recommend venues based on your budget, guest count, and event type."

        # Payment
        elif "payment" in user_message:
            bot_reply = "Payments can be made via UPI, debit/credit card, or online bank transfer."

        # Refund
        elif "refund" in user_message or "cancellation" in user_message:
            bot_reply = "Refunds depend on the cancellation date and event type. Please contact support for details."

        # Contact
        elif "contact" in user_message or "email" in user_message or "phone" in user_message:
            bot_reply = "You can contact Evento at contact@evento.com or call +91 9876543210."

        # Reviews
        elif "review" in user_message or "feedback" in user_message:
            bot_reply = "Customer reviews and ratings are available on each venue’s detail page."

        # Create Venue
        elif "create venue" in user_message or "add venue" in user_message:
            bot_reply = (
                "To create a venue:\n"
                "1. Login to Evento\n"
                "2. Go to Venue section\n"
                "3. Click Create Venue\n"
                "4. Enter venue details\n"
                "5. Submit for approval"
            )

        # Themes
        elif "theme" in user_message or "wedding theme" in user_message:
            bot_reply = "We offer traditional, royal, floral, beach, and modern wedding themes."

        # After Booking
        elif "after booking" in user_message or "booking confirmation" in user_message:
            bot_reply = "After booking, you will receive confirmation, invoice, and QR code. Our team will contact you."

        else:
            bot_reply = "Thank you for contacting Evento. Please ask about booking, venues, services, or pricing."

        return JsonResponse({"response": bot_reply})

    return JsonResponse({"response": "Invalid request method."})