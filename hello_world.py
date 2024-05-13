@service
def hello_world(action=None, id=None):
    """hello_world example using pyscript."""
    name = state.getattr('event.brian_s_room_switch_button_3')
    log.info(f"hello world: got name {name} id {id}")
    if action == "turn_on" and id is not None:
        light.turn_on(entity_id=id, brightness=255)
    elif action == "fire" and id is not None:
        event.fire(id, param1=12, pararm2=80)