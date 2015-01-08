import dynamic
import analysis_2
import os

def test(audio_1, audio_2):
    seqx = get_seq(audio_1)
    seqy = get_seq(audio_2)
    return dynamic.dynamicTimeWarp(seqx,seqy)

def get_seq(audio):
    return analysis_2.master(os.path.abspath(audio))



#should match(new password)
print "match-new passphrase"
print test("audios/open_pod.wav", "audios/open_pod_2.wav")
#should not match(new password)
print "no match-new password"
print test("audios/open_pod.wav", "audios/Mitzi.wav")















