from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class ChatbotUserThrottle(UserRateThrottle):
    rate = '100/hour'

class ChatbotAnonThrottle(AnonRateThrottle):
    rate = '20/hour' 