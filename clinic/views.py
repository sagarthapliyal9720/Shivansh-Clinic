from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def appointment(request):

    if request.method == "POST":

        # Get form data
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        date = request.POST.get("date", "").strip()
        reason = request.POST.get("reason", "").strip()


        # Basic validation
        if not name or not phone or not date:

            return render(
                request,
                "appointment.html",
                {
                    "error": "Please fill all required fields."
                }
            )


        # Appointment email content
        subject = f"New Appointment Request - {name}"


        message = f"""
New Appointment Request
Shivansh Clinic

Doctor: Dr. Kapil Sharma
Qualification: B.A.M.S
Specialization: General Physician

-----------------------------------

Patient Name: {name}
Phone Number: {phone}
Patient Email: {email if email else "Not provided"}
Preferred Date: {date}

Reason for Visit:
{reason if reason else "Not provided"}

-----------------------------------

This appointment request was submitted
through the Shivansh Clinic website.
"""


        try:

            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DOCTOR_EMAIL],
                fail_silently=False,
            )


            # Success message shown to user
            return render(
                request,
                "appointment.html",
                {
                    "success": (
                        "Your appointment request has been sent successfully. "
                        "Our team will contact you soon."
                    )
                }
            )


        except Exception:

            return render(
                request,
                "appointment.html",
                {
                    "error": (
                        "Something went wrong while sending your request. "
                        "Please try again or contact the clinic directly."
                    )
                }
            )


    return render(request, "appointment.html")


def gallery(request):
    return render(request, "gallery.html")


def testimonials(request):
    return render(request, "testimonials.html")


def contact(request):
    return render(request, "contact.html")