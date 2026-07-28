"""
Scenario: You are building a notification system for an app. 
The function needs to accept a mandatory message, followed by any additional
positional information, and finally optional settings configuration.
Goal: Create a function send_alert(message, *details, **settings) that returns
a cleanly formatted dictionary.Expected Behavior:
    Calling send_alert("System Overload", "Server-01", "Rack-4", dynamic_priority=True, sound="Siren")
    should return: 
        python{
        "alert": "System Overload",
        "meta_info": ("Server-01", "Rack-4"),
        "config": {"dynamic_priority": True, "sound": "Siren"}
    }
"""
def send_alert(message,*args,**kwargs):
    return f"alert: {message} \nmeta_info: {args} \nconfig: {kwargs}"
print(send_alert("System Overload", "Server-01", "Rack-4", dynamic_priority=True, sound="Siren"))