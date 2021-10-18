text = "X-DSPAM-Confidence:    0.8475"
posB = text.find("0")
posE = text.find("5")
print(float(text[posB:posE+1]))
