class Gravity():
	def __init__(self,gravity_scaling = 0.995, reduction = 5, jump_increase = 5, max_gravity = 10):
		self.y_velocity = 0

		self.gravity_scaling = 0.991
		self.reduction = 7
		self.jump_increase = 5
		self.max_gravity = 10

	def tick(self) -> float:
		self.y_velocity -= self.gravity_scaling / self.reduction
		self.y_velocity *= self.gravity_scaling

		if self.y_velocity > self.max_gravity: self.y_velocity = self.y_velocity

		return self.y_velocity

	def jump(self) -> float:
		self.y_velocity = self.jump_increase

		return self.y_velocity

class Bounce():
	def __init__(self,value: float = 0.8,min_gravity: float = 0.1):
		self.value = value
		self.min_gravity = min_gravity

	def tick(self,velocity: float) -> float:
		if velocity > self.min_gravity:
			return velocity * self.value * -1
		else:
			return 0