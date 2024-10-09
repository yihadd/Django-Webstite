from django.utils.deprecation import MiddlewareMixin
from .models import Visitor

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        session_key = request.session.session_key
        if not session_key:
            # Create a new session if one doesn't exist
            request.session.create()
            session_key = request.session.session_key

        ip_address = self.get_client_ip(request)

        # Check if the visitor already exists based on their session key
        if not Visitor.objects.filter(session_key=session_key).exists():
            # Store the visitor in the database
            Visitor.objects.create(ip_address=ip_address, session_key=session_key)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
