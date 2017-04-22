import pickle
import tagTweets

def save_obj(obj,name):
  with open(name + '.pkl', 'wb') as f:
    pickle.dump(obj,f,pickle.HIGHEST_PROTOCOL)

def load_obj(name):
  with open(name + '.pkl','rb') as f:
    return pickle.load(f) 

def POSprob(taggedwords):
    d = dict.fromkeys(['S#','F#']) 
    d['S#'] = []
    d['F#'] = []
    nowtag = ""
    nexttag = ""
    # lst is Tweet (list of tuples)
    for lst in taggedwords:
        # deal with start in outer loop
        nowtag = "S#"
        nexttag = lst[0][1] 

        taglist = [x[0] for x in d[nowtag]]
        if nexttag in taglist:
	  for t in d[nowtag]:
            if nexttag == t[0]:
              t[1] += 1
        else:
          d[nowtag] += [[nexttag, 1]] 

        for i in range(len(lst)-1):
          nowtag = lst[i][1]
          # set nexttag
          if i == len(lst)-1:
                nexttag = "F#"
          else:
            nexttag = lst[i+1][1]

          if nowtag in d:
            # make list of tags currently following nowtag
            taglist = [x[0] for x in d[nowtag]]
            if nexttag in taglist:
              for t in d[nowtag]:
                if nexttag == t[0]:
                  t[1] += 1
            else:
              d[nowtag] += [[nexttag, 1]]
          else:
            d[nowtag] = [[nexttag, 1]]
    return d

save_obj(POSprob(load_obj('tweetsPOS')), 'followsPOS')


