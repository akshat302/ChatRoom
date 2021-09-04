from channels.auth import AuthMiddlewareStack      #To identify the user
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing


application = ProtocolTypeRouter({
   'websocket': AuthMiddlewareStack(
       URLRouter (
           chat.routing.websocket_urlpatterns,
       )
   ),
})
