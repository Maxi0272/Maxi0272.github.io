extends KinematicBody2D

var velocity = Vector2.ZERO

const maxspeed = 100
const accel = 600
const friction = 600

func _physics_process(delta):
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left") 
	input_vector.y = Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up") 
	input_vector = input_vector.normalized()
	
	if  input_vector != Vector2.ZERO:
		velocity = velocity.move_toward(input_vector * maxspeed, accel * delta)
		
	else:
		velocity = velocity.move_toward(Vector2.ZERO, friction * delta)
	velocity = move_and_slide(velocity)
