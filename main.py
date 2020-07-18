from PIL import Image, ImageDraw, ImageFont
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import math

# Display size
width = 2256 #FIXME
height = 1504 #FIXME

block_size = 25
block_gap = 25
xoffset = 25
yoffset = 25

red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

im = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(im)
# fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
fnt = ImageFont.truetype("arial.ttf", size=20)

today = date.today() 
# DateOfBirth
birthdate = #FIXME date(year, month, day)
# male
life_expectancy = 86 #FIXME # https://www.ons.gov.uk/peoplepopulationandcommunity/helthandsocialcare/healthandlifeexpectancies/lifeexpectancycalculator/2019-06-07
#life_expectancy = 71.8 # years https://www.worldlifeexpectancy.com/thailand-life-expectancy 
# female
#life_expectancy = 79.3
#life_expectancy = 89 # ons.gov.uk

life_expectancy_month = life_expectancy * 12
estimated_death_date = birthdate + relativedelta(months=+math.floor(life_expectancy_month))

delta = relativedelta(today, birthdate)

print("BirthDate:", birthdate)
print("Today:", today)
print("Age:", delta.years, "years", delta.months, "months", delta.days, "days")
print("EstimatedDeath?:", estimated_death_date)

month = 0
for i in range(height//(block_size+block_gap)):
	for j in range(width//(block_size+block_gap)):
		# top left corner
		x0 = xoffset + j * (block_size + block_gap)
		y0 = yoffset + i * (block_size + block_gap)
		# bottom right corner
		x1 = x0 + block_size
		y1 = y0 + block_size
		# print(x0,y0,x1,y1)
		if (birthdate + relativedelta(months=month) < today):
			draw.rectangle((x0,y0,x1,y1), fill=red, outline=black)
		elif (birthdate + relativedelta(months=month) >= estimated_death_date):
			draw.rectangle((x0,y0,x1,y1), fill=white, outline=black)
		else:
			draw.rectangle((x0,y0,x1,y1), fill=green, outline=black)
		if (month % 10 == 0):
			draw.text((x0,y0), str(month), font=fnt, fill=black)
		# draw.text((x0,y0), str(month), fill=black)
		month += 1

print("Total displayed months:", month)
print("Total displayed years:", month // 12)

# im.show()
im.save('./test.jpg')
