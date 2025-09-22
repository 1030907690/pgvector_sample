from sentence_transformers import SentenceTransformer, util
from PIL import Image
import os

#Load CLIP model
model = SentenceTransformer('clip-ViT-B-32')

print("model")
#Encode an image:
img_emb = model.encode(Image.open('sc.png'))
print('img_emb')
#Encode text descriptions
text_emb = model.encode(['Two dogs in the snow', 'A cat on a table', 'A picture of London at night'])
print('text_emb')
#Compute cosine similarities
cos_scores = util.cos_sim(img_emb, text_emb)
print(len(img_emb.tolist()))
print(img_emb.tolist())
# print(cos_scores)
