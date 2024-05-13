from homeassistant.const import EVENT_STATE_CHANGED

registered_triggers = []

#def make_air_conditioner(config): 
#    @time_trigger(f"{config['nighttime']}")
#    def nighttime_handler():
#        if new_state.attributes['event_type'] != "initial_press":
#            return
#        log.info(config)
#        for light in config['lights']:
#            set_light(light['light_id'], light['brightness'])
#    
#    registered_triggers.append(nighttime_handler)
#    
#    
#    
#    @time_trigger(f"{config['daytime']}")
#    def daytime_handler():
#        if sensor.london_high_temperature > config['daytime_temp_threshold']:
#            config['entity_id']
#    
#    registered_triggers.append(brightness_up_button_handler)
#    
#    
#    @event_trigger(EVENT_STATE_CHANGED, f"entity_id == 'event.{config['switch_name']}_button_3'")
#    @time_active(f"range({config['start_time']}, {config['end_time']})")
#    @task_unique(f"button_handler_{config['switch_name']}_brightness_off", kill_me=True)
#    def brightness_down_button_handler(entity_id=None, old_state=None, new_state=None):        
#        if new_state.attributes['event_type'] != "initial_press":
#            return
#            
#        for light in config['lights']:
#            target_brightness = get_light_brightness(light['light_id']) - 30
#            set_light(light['light_id'], target_brightness)
#                
#    registered_triggers.append(brightness_down_button_handler)
#                
#                
#    @event_trigger(EVENT_STATE_CHANGED, f"entity_id == 'event.{config['switch_name']}_button_4'")
#    @time_active(f"range({config['start_time']}, {config['end_time']})")
#    @task_unique(f"button_handler_{config['switch_name']}_off", kill_me=True)
#    def off_button_handler(entity_id=None, old_state=None, new_state=None):
#        if new_state.attributes['event_type'] != "initial_press":
#            return
#            
#        for light in config['lights']:
#            set_light(light['light_id'], 0)
#                
#    registered_triggers.append(off_button_handler)
#
#@time_trigger
#def air_conditioner_startup():
#    for app in pyscript.app_config:
#        make_air_conditioner(app)