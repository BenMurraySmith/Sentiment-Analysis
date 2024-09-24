import spacy # type: ignore
nlp = spacy.load("en_core_web_sm")
updated_stopwords = ['one', 'own', 'least', 'through', 'can', 'become', 'six', '�ll', 'full', 'when', 'seems', 'both', 'seem', 'forty', 'been', 'all', 'whereby', 'those', 'everywhere', 'because', 'here', 'put', 'anything', 'whither', 'many', 'really', 'something', 'beforehand', 'per', '�s', 'always', 'will', "'ll", '�d', 'had', 'by', 'must', 'becomes', 'wherein', 'part', 'else', 'since', 'in', 'third', 'latterly', 'they', 'where', 'nine', 'four', 'why', 'somehow', 'unless', 'or', 'about', 'herein', "'d", 'three', 'anyone', 'may', 'might', 'therein', 'except', 'my', 'that', 'even', 'ca', 'be', 'perhaps', 'himself', 'same', 'most', 'elsewhere', 'thereafter', 'does', 'ours', '�d', 'just', 'anyhow', 'below', 'did', 'keep', 'cannot', 'behind', 'go', 'during', 'get', '�s', 'against', 'his', "'re", 'what', 'whereafter', 'have', 'everyone', 'everything', 'would', 'whereupon', 'two', 'throughout', 'whether', 'further', 'before', 'such', 'their', 'together', 'as', 'side', 'being', 'are', 'then', 'of', 'any', 'an', 'mostly', 'rather', 'take', 'around', 'hence', 'each', 'others', '�re', 'eight', 'at', 'please', 'whatever', 'whose', 'nor', 'itself', 'after', 'noone', 'whole', 'someone', 'becoming', 'top', 'her', 'now', 'seemed', 'eleven', 'first', 'move', '�re', 'twelve', "'m", 'out', 'our', 'latter', 'n�t', 'make', 'yourself', 'less', 'ten', 'much', 'across', 'seeming', 'thereupon', 'indeed', 'this', 'over', 'used', 'whence', 'whoever', 'back', 'hereupon', "'ve", 'last', 'anyway', 'quite', 'thereby', 'hereby', 'moreover', 'so', 'often', 'wherever', 'again', 'were', 'afterwards', 'myself', 'who', 'whom', '�ve', 'with', 'more', 're', 'became', 'towards', 'sometimes', 'it', 'various', 'beyond', 'fifty', 'amount', 'almost', 'toward', 'onto', 'empty', 'next', 'from', 'up', 'your', 'several', '�ll', 'we', 'also', 'bottom', 'give', 'thus', 'under', 'i', 'using', 'therefore', 'another', 'only', 'doing', '�ve', 'above', 'whereas', 'somewhere', 'them', 'regarding', 'thru', 'very', 'five', 'made', 'than', 'down', 'front', 'namely', 'meanwhile', 'sometime', 'anywhere', 'could', 'name', 'until', 'along', '�m', 'thence', 'once', 'via', 'ourselves', 'the', 'upon', '�m', 'has', 'besides', 'ever', 'whenever', 'am', 'for', 'which', 'is', 'these', 'hundred', 'fifteen', 'call', 'enough', 'hereafter', 'too', 'every', 'she', 'herself', 'beside', 'few', 'how', 'hers', 'us', 'there', 'among', 'formerly', 'sixty', 'twenty', 'serious', 'mine', 'do', 'see', 'well', 'already', 'was', 'yourselves', 'he', 'off', 'on', 'yours', 'either', 'should', 'between', 'you', 'while', 'its', 'due', 'show', 'amongst', 'if', 'to', 'say', 'some', 'within', 'into', "'s", 'him', 'a', 'and', 'themselves', 'alone', 'former', 'done', 'me', 'other', 'n�t', 'otherwise']
negation_tokens = [
    "not", 
    "n't", 
    "no", 
    "never", 
    "none", 
    "nothing", 
    "nowhere", 
    "neither", 
    "nobody", 
    "without", 
    "hardly", 
    "scarcely", 
    "barely"
]
contradiction_tokens = [
    "but", 
    "however", 
    "nevertheless", 
    "nonetheless", 
    "yet", 
    "although", 
    "though", 
    "still", 
    "even so", 
    "on the other hand", 
    "despite", 
    "in spite of", 
    "conversely"
]
