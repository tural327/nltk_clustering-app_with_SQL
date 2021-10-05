# Server Error Message Clustering

Main point of this project is grouping error message I think that will be increase productivity. Messages will be save mysql server.

Before applying clustering we need making cleaning our dataset I need make a cleaning. Messages format is **'eit-prismadm01.tgna.tegna.com: System or agent has recently restarted'** we need to take only **"System or agent has recently restarted"** section for make more accurate CountVectorizer() arrays.
After making text cleaning I made to display most frequent words

![](https://github.com/tural327/nltk_clustering-app_with_SQL/blob/master/images_for_README/words.png)

After cleaning I saved vectorized words (that will be using at the end of for my web application)

For next I need find optimal cluster number for that reason I used find optimal cluster by using displaying errors:

![](https://github.com/tural327/nltk_clustering-app_with_SQL/blob/master/images_for_README/find_clstr_value.png)

I will be use 5 cluster for my model

For GaussianMixture model by using n_components=5 I got:

![](https://github.com/tural327/nltk_clustering-app_with_SQL/blob/master/images_for_README/GaussianMixture.png)

If we applied KMeans(n_clusters=5) I got :

![](https://github.com/tural327/nltk_clustering-app_with_SQL/blob/master/images_for_README/kmean.png)

GaussianMixture model was more smooth clustering I will be save that model for my Flask server

# Flask & Mysql 
I made simple [Flask](https://github.com/tural327/nltk_clustering-app_with_SQL/tree/master/Flask)

* For making connection with my server and adding error message I made a simple script [server.py](https://github.com/tural327/nltk_clustering-app_with_SQL/blob/master/Flask/server.py). I just using simple MYSQL code for adding and making commit for connection 
* While adding text I need clean my text so for that reason I made [main.py](https://github.com/tural327/nltk_clustering-app_with_SQL/blob/master/Flask/main.py) script - script contain same cleaning function on [main](https://github.com/tural327/nltk_clustering-app_with_SQL/blob/master/clustering.ipynb) file
* Main [app.py](https://github.com/tural327/nltk_clustering-app_with_SQL/blob/master/Flask/app.py) file I used :
```python
        my_text = str(request.form.get("msg"))
        result = len(my_text)
        if result >0:
 ```
 
 Because we need avoid error while text not added and just show table.....
 
 While adding error message data.csv file will be update which is containing last data on table and saving 
 
