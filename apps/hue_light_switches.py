from homeassistant.const import EVENT_STATE_CHANGED

registered_triggers = []

def set_light(light_id, target):
    if target <= 0:
        light.turn_off(entity_id=light_id)
    else:
        light.turn_on(entity_id=light_id, brightness=target)

def get_light_brightness(light_id):
    curr_brightness = state.getattr(light_id)['brightness']
    if curr_brightness == None:
        curr_brightness = 0
        
    log.info(curr_brightness)
    return curr_brightness

def make_hue_light_switch(config): 
    @event_trigger(EVENT_STATE_CHANGED, f"entity_id == 'event.{config['switch_name']}_button_1'")
    @time_active(f"range({config['start_time']}, {config['end_time']})")
    @task_unique(f"button_handler_{config['switch_name']}_on", kill_me=True)
    def on_button_handler(entity_id=None, old_state=None, new_state=None):
        if new_state.attributes['event_type'] != "initial_press":
            return
        log.info(config)
        for light in config['lights']:
            log.info(light)
            set_light(light['light_id'], light['brightness'])
    
    registered_triggers.append(on_button_handler)
    
    
    @event_trigger(EVENT_STATE_CHANGED, f"entity_id == 'event.{config['switch_name']}_button_2'")
    @time_active(f"range({config['start_time']}, {config['end_time']})")
    @task_unique(f"button_handler_{config['switch_name']}_brightness_up", kill_me=True)
    def brightness_up_button_handler(entity_id=None, old_state=None, new_state=None):        
        if new_state.attributes['event_type'] != "initial_press":
            return
            
        for light in config['lights']:
            target_brightness = get_light_brightness(light['light_id']) + 30
            set_light(light['light_id'], target_brightness)
    
    registered_triggers.append(brightness_up_button_handler)
    
    
    @event_trigger(EVENT_STATE_CHANGED, f"entity_id == 'event.{config['switch_name']}_button_3'")
    @time_active(f"range({config['start_time']}, {config['end_time']})")
    @task_unique(f"button_handler_{config['switch_name']}_brightness_off", kill_me=True)
    def brightness_down_button_handler(entity_id=None, old_state=None, new_state=None):        
        if new_state.attributes['event_type'] != "initial_press":
            return
            
        for light in config['lights']:
            target_brightness = get_light_brightness(light['light_id']) - 30
            set_light(light['light_id'], target_brightness)
                
    registered_triggers.append(brightness_down_button_handler)
                
                
    @event_trigger(EVENT_STATE_CHANGED, f"entity_id == 'event.{config['switch_name']}_button_4'")
    @time_active(f"range({config['start_time']}, {config['end_time']})")
    @task_unique(f"button_handler_{config['switch_name']}_off", kill_me=True)
    def off_button_handler(entity_id=None, old_state=None, new_state=None):
        if new_state.attributes['event_type'] != "initial_press":
            return
            
        for light in config['lights']:
            set_light(light['light_id'], 0)
                
    registered_triggers.append(off_button_handler)

@time_trigger
def hue_light_switch_startup():
    for app in pyscript.app_config:
        make_hue_light_switch(app)