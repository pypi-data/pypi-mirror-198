import numpy as np
from time import time, sleep
import random
import colors
import os


class Donut:

	def __init__(self, count=1, color="rgb(255,255,255)", speed=1, symbolGradient=".:!/r(l1Z4H9W8$@", mode="full"):
		os.system('')

		self.colors = []

		if color == "rainbow":
			for i in range(0, 256, 3):
				self.colors.append(f'rgb({255 - i}, 0, {i})')

			for i in range(0, 256, 3):
				self.colors.append(f'rgb(0, {i}, {255 - i})')

			for i in range(0, 256, 3):
				self.colors.append(f'rgb({i}, {255 - i}, 0)')
		elif color=="random":
			self.colors.append(f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})")
		else:
			self.colors.apend(color)
		if len(symbolGradient) < 12:
			raise ValueError("Symbol gradient must have more than 11 symbols!")

		if speed <= 0:
			raise ValueError("Speed must be granter than 0")
		else:
			self.speed = speed

		self.mode = mode

		self.frame = 0

		self.count = count
		self.screen_size = int(42*((2-int(self.count == 1))/self.count))
		self.theta_spacing = 0.07
		self.phi_spacing = 0.02
		self.illumination = np.fromiter(symbolGradient, dtype="<U1")

		self.fps = 1000 / 60

		self.A = 0
		self.B = 0
		self.R1 = 1
		self.R2 = 2
		self.K2 = 5
		self.K1 = self.screen_size * self.K2 * 3 / (8 * (self.R1 + self.R2))

	def render_frame(self, A, B):
		startTime = time()
		cos_A = np.cos(A)
		sin_A = np.sin(A)
		cos_B = np.cos(B)
		sin_B = np.sin(B)

		output = np.full((self.screen_size, self.screen_size), " ")  # (40, 40)
		zbuffer = np.zeros((self.screen_size, self.screen_size))  # (40, 40)
		phi = np.arange(0, 2 * np.pi, self.phi_spacing)
		cos_phi = np.cos(phi)  # (315,)
		sin_phi = np.sin(phi)  # (315,)
		theta = np.arange(0, 2 * np.pi, self.theta_spacing)
		cos_theta = np.cos(theta)  # (90,)
		sin_theta = np.sin(theta)  # (90,)
		circle_x = self.R2 + self.R1 * cos_theta  # (90,)
		circle_y = self.R1 * sin_theta  # (90,)

		x = (np.outer(cos_B * cos_phi + sin_A * sin_B * sin_phi, circle_x) - circle_y * cos_A * sin_B).T  # (90, 315)
		y = (np.outer(sin_B * cos_phi - sin_A * cos_B * sin_phi, circle_x) + circle_y * cos_A * cos_B).T  # (90, 315)
		z = ((self.K2 + cos_A * np.outer(sin_phi, circle_x)) + circle_y * sin_A).T  # (90, 315)
		ooz = np.reciprocal(z)  # Calculates 1/z
		xp = (self.screen_size / 2 + self.K1 * ooz * x).astype(int)  # (90, 315)
		yp = (self.screen_size / 2 - self.K1 * ooz * y).astype(int)  # (90, 315)
		L1 = (((np.outer(cos_phi, cos_theta) * sin_B) - cos_A * np.outer(sin_phi,
																		 cos_theta)) - sin_A * sin_theta)  # (315, 90)
		L2 = cos_B * (cos_A * sin_theta - np.outer(sin_phi, cos_theta * sin_A))  # (315, 90)
		L = np.around(((L1 + L2) * 8)).astype(int).T  # (90, 315)
		mask_L = L >= 0  # (90, 315)
		chars = self.illumination[L]  # (90, 315)

		for i in range(90):
			mask = mask_L[i] & (ooz[i] > zbuffer[xp[i], yp[i]])  # (315,)

			zbuffer[xp[i], yp[i]] = np.where(mask, ooz[i], zbuffer[xp[i], yp[i]])
			output[xp[i], yp[i]] = np.where(mask, chars[i], output[xp[i], yp[i]])

		return {"out": output, "stoptime": time(), "starttime": startTime}

	def pprint(self, array):
		arr = []
		if self.mode == "full":
			curColor = self.colors[self.frame % len(self.colors)]
			for row in array:
				arr.append(colors.color(" ".join(row), fg=curColor) * self.count)
		elif self.mode == "linear":
			for row in array:
				curColor = self.colors[self.frame % len(self.colors)]
				arr.append(colors.color(" ".join(row), fg=curColor) * self.count)
				self.frame += 1
			self.frame = self.frame - len(arr) + 1
		print(*arr, sep="\n")
		self.frame += 1
		if self.frame % len(self.colors) == 0:
			self.frame = 0

	def start(self):
		while True:
			self.A += self.theta_spacing*self.speed
			self.B += self.phi_spacing*self.speed
			print("\x1b[H")

			fr = self.render_frame(self.A, self.B)

			sleep((self.fps - (fr["stoptime"] - fr["starttime"])) / 1000)

			self.pprint(fr["out"])


if __name__ == "__main__":
	donut = Donut(2, "rainbow", speed=1, mode="linear")
	donut.start()

