# Django based credit rating

The aim of this app is to predict a credit risk by giving a score instead ofthe probability default.  The back end part was made with pythondjangoframework,  scikit  learn,  pandasandbokehlibraries.   For  the  frondend,html, cssandbootstrapwere used.  The grade is a transformation ofprobability coefficients obtained with logistic regression to the range 0-100.

The data are about credit for cars acquisition from a french local bank.  Allloans were granted between 01/02/2004 and 12/19/2009.  The database con-tains 15 variables.  After usingV- Cramercorrelation test, only 4 variableswere significant for the default prediction:1.amount:  Amount of the initial credit2.age:  The age at the moment of subscription3.duration:  The duration of the credit to be refunded4.rate:  The rate at the moment of subscription
