# kprototype_clustering
## Reference Link(for original Dataset):
1. <a href="https://www.kaggle.com/henriqueyamahata/bank-marketing">Dataset</a>

## Dataset Details (for <a href="https://raw.githubusercontent.com/saujanya01/kprototype_clustering/master/customer_data.csv">Modified Dataset</a>):

### Related to customer
1 - age (numeric)

2 - job : type of job (categorical: "admin.","blue-collar","entrepreneur","housemaid","management","retired","self-employed","services","student","technician","unemployed","unknown")

3 - marital : marital status (categorical: "divorced","married","single","unknown"; note: "divorced" means divorced or widowed)

4 - education (categorical: "basic.4y","basic.6y","basic.9y","high.school","illiterate","professional.course","university.degree","unknown")

5 - default: has credit in default? (categorical: "no","yes","unknown")

6 - housing: has housing loan? (categorical: "no","yes","unknown")

7 - loan: has personal loan? (categorical: "no","yes","unknown")

### related with the last contact of the current campaign:

8 - comm_type: contact communication type (categorical: "cellular","telephone") 

9 - month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")

10 - day_of_week: last contact day of the week (categorical: "mon","tue","wed","thu","fri")

11 - last_contact_duration: last contact duration, in seconds (numeric). Important note:  this attribute highly affects the output target (e.g., if duration=0 then y="no"). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.

### other attributes(contact behaviour):

12 - campaign_contact_count: number of contacts performed during this campaign and for this client (numeric, includes last contact)

13 - poutcome: outcome of the previous marketing campaign (categorical: "failure","nonexistent","success")

### social and economic context attributes

14 - cons.price.idx: consumer price index - monthly indicator (numeric)     

15 - cons.conf.idx: consumer confidence index - monthly indicator (numeric)     

16 - nr.employed: number of employees - quarterly indicator (numeric)(drop)

## Dataset after clustering(a new column 'cluster' has been added)
<a href="https://raw.githubusercontent.com/saujanya01/kprototype_clustering/master/with_cluster_full.csv">Click Here</a>
<a href="https://github.com/saujanya01/kprototype_clustering/blob/master/customer_clustering.ipynb">Notebook with Clustering</a>
<a href="https://github.com/saujanya01/kprototype_clustering/blob/master/plots.ipynb">Notebook with plots</a>