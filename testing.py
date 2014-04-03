import dynamic
import analysis_2
import os

def test(audio_1, audio_2):
    seqx = get_seq(audio_1)
    seqy = get_seq(audio_2)
    return dynamic.dynamicTimeWarp(seqx,seqy)

def get_seq(audio):
    return analysis_2.master(os.path.abspath(audio))




# #should match perfectly
# print "perfect match"

# print test("audios/Alohamora_3.wav", "audios/Alohamora_3.wav")

# print test("audios/Alohamora_2.wav", "audios/Alohamora_2.wav")

# print test("audios/Alohamora_5.wav", "audios/Alohamora_5.wav")

# #should match
# print "match"

# print test("audios/Alohamora_3.wav", "audios/Alohamora_2.wav")

# print test("audios/Alohamora_3.wav", "audios/Alohamora_5.wav")

# print test("audios/Alohamora_2.wav", "audios/Alohamora_5.wav")

# #word matches but person is different
# print "Lizz"

# print test("audios/Alohamora_3.wav", "audios/Lizz_Alohamora.wav")

# print test("audios/Alohamora_2.wav", "audios/Lizz_Alohamora.wav")

# print test("audios/Alohamora_5.wav", "audios/Lizz_Alohamora.wav")

# print "Katrina"

# print test("audios/Alohamora_3.wav", "audios/Katrina_Alohamora.wav")

# print test("audios/Alohamora_2.wav", "audios/Katrina_Alohamora.wav")

# print test("audios/Alohamora_5.wav", "audios/Katrina_Alohamora.wav")

# print "Kristin"

# print test("audios/Alohamora_3.wav", "audios/Kristin_Alohamora.wav")

# print test("audios/Alohamora_2.wav", "audios/Kristin_Alohamora.wav")

# print test("audios/Alohamora_5.wav", "audios/Kristin_Alohamora.wav")

# print "Mom"

# print test("audios/Alohamora_3.wav", "audios/Mom_Alohamora.wav")

# print test("audios/Alohamora_2.wav", "audios/Mom_Alohamora.wav")

# print test("audios/Alohamora_5.wav", "audios/Mom_Alohamora.wav")

# print test("audios/Alohamora_3.wav", "audios/Mom_Alohamora_2.wav")

# print test("audios/Alohamora_2.wav", "audios/Mom_Alohamora_2.wav")

# print test("audios/Alohamora_5.wav", "audios/Mom_Alohamora_2.wav")

# print "Audrey"

# print test("audios/Alohamora_3.wav", "audios/Audrey_Alohamora.wav")

# print test("audios/Alohamora_2.wav", "audios/Audrey_Alohamora.wav")

# print test("audios/Alohamora_5.wav", "audios/Audrey_Alohamora.wav")

# print test("audios/Alohamora_3.wav", "audios/Audrey_Alohamora_2.wav")

# print test("audios/Alohamora_2.wav", "audios/Audrey_Alohamora_2.wav")

# print test("audios/Alohamora_5.wav", "audios/Audrey_Alohamora_2.wav")

# print "Tim"

# print test("audios/Alohamora_3.wav", "audios/Tim_Alohamora.wav")

# print test("audios/Alohamora_2.wav", "audios/Tim_Alohamora.wav")

# print test("audios/Alohamora_5.wav", "audios/Tim_Alohamora.wav")

# print test("audios/Alohamora_3.wav", "audios/Tim_Alohamora_2.wav")

# print test("audios/Alohamora_2.wav", "audios/Tim_Alohamora_2.wav")

# print test("audios/Alohamora_5.wav", "audios/Tim_Alohamora_2.wav")

# print "Hunter"

# print test("audios/Alohamora_3.wav", "audios/Hunter_Alohamora.wav")

# print test("audios/Alohamora_2.wav", "audios/Hunter_Alohamora.wav")

# print test("audios/Alohamora_5.wav", "audios/Hunter_Alohamora.wav")

# print test("audios/Alohamora_3.wav", "audios/Hunter_Alohamora_2.wav")

# print test("audios/Alohamora_2.wav", "audios/Hunter_Alohamora_2.wav")

# print test("audios/Alohamora_5.wav", "audios/Hunter_Alohamora_2.wav")

# #words should not match
# print "person match but no word match"

# print "Alohamora vs testing_2"

# print test("audios/Alohamora_3.wav", "audios/testing_2.wav")

# print test("audios/Alohamora_2.wav", "audios/testing_2.wav")

# print test("audios/Alohamora_5.wav", "audios/testing_2.wav")

# print "Alohamora vs aloplethora"

# print test("audios/Alohamora_3.wav", "audios/aloplethora.wav")

# print test("audios/Alohamora_2.wav", "audios/aloplethora.wav")

# print test("audios/Alohamora_5.wav", "audios/aloplethora.wav")

# print "no person or word match"

# print "Mom"

# print test("audios/Alohamora_3.wav", "audios/Mom_testing.wav")

# print test("audios/Alohamora_2.wav", "audios/Mom_testing.wav")

# print test("audios/Alohamora_5.wav", "audios/Mom_testing.wav")

# print "Audrey"

# print test("audios/Alohamora_3.wav", "audios/Audrey_testing.wav")

# print test("audios/Alohamora_2.wav", "audios/Audrey_testing.wav")

# print test("audios/Alohamora_5.wav", "audios/Audrey_testing.wav")

# print "Tim"

# print test("audios/Alohamora_3.wav", "audios/Tim_testing.wav")

# print test("audios/Alohamora_2.wav", "audios/Tim_testing.wav")

# print test("audios/Alohamora_5.wav", "audios/Tim_testing.wav")

# print "Hunter"

# print test("audios/Alohamora_3.wav", "audios/Hunter_testing.wav")

# print test("audios/Alohamora_2.wav", "audios/Hunter_testing.wav")

# print test("audios/Alohamora_5.wav", "audios/Hunter_testing.wav")

# print "blank vs alohamora"

# print test("audios/Alohamora_3.wav", "audios/blank_1.wav")

# print test("audios/Alohamora_2.wav", "audios/blank_1.wav")

# print test("audios/Alohamora_5.wav", "audios/blank_1.wav")

# print test("audios/Alohamora_3.wav", "audios/blank_2.wav")

# print test("audios/Alohamora_2.wav", "audios/blank_2.wav")

# print test("audios/Alohamora_5.wav", "audios/blank_2.wav")

# print test("audios/Alohamora_3.wav", "audios/blank_3.wav")

# print test("audios/Alohamora_2.wav", "audios/blank_3.wav")

# print test("audios/Alohamora_5.wav", "audios/blank_3.wav")

# print test("audios/Alohamora_3.wav", "audios/blank_4.wav")

# print test("audios/Alohamora_2.wav", "audios/blank_4.wav")

# print test("audios/Alohamora_5.wav", "audios/blank_4.wav")










