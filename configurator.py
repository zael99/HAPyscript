import requests
import json


@service("configurator.activate_profile")
def activate_profile(profile=None):
    headers = {
        'accept': 'application/json',
        'auth': pyscript.config['global']['configurator_auth'],
    }

    response = task.executor(requests.post, f"http://192.168.0.109:7293/api/Profile/activate/{profile}", headers=headers)
    log.info(response)
        
@service("configurator.get_profiles", supports_response="only")
def get_profiles():
    headers = {
        'accept': 'application/json', 
        'auth': pyscript.config['global']['configurator_auth'],
    }

    response = task.executor(requests.get, f"http://192.168.0.109:7293/api/Profile/", headers=headers)
    
    output = {
        "profiles" : json.loads(response.text)
    }
    
    return output
    
@service("configurator.get_active_profile")
def get_active_profiles():
    headers = {
        'accept': 'application/json',
        'auth': pyscript.config['global']['configurator_auth'],
    }

    response = task.executor(requests.get, f"http://192.168.0.109:7293/api/Profile/active", headers=headers)
    
    output = {
        "active_profile" : json.loads(response.text)
    }
    
    return output
    

@time_trigger("cron(*/1 * * * *)")
def update_sensors():
    
    active_profile_data = get_active_profiles()
    
    entity = "sensor.configurator_active_profile"
    attributes = {}
    attributes["display_state"] = active_profile_data["active_profile"]
    attributes["display_icon"] = "mdi:check-circle-outline"
    attributes["attribution"] = "Configurator"
    attributes['friendly_name'] = "Configurator Active Profile"
    state.set(entity, active_profile_data["active_profile"])