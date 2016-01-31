dataset <- read.csv('/users/nandu/desktop/PROJECT/3REDNORM.csv', head=FALSE)
index <- 1:nrow(dataset)
testindex <- sample(index, trunc(length(index)*30/100))
testset <- dataset[testindex,]
trainset <- dataset[-testindex,]

tuned <- tune.svm(V1~., data = trainset, gamma = 10^(-6:-1), cost = 10^(-1:1))
summary(tuned)
svm_model  <- svm(V1~., data = trainset, kernel="radial", gamma=0.01, cost=10)
summary(svm_model)
svm_prediction <- predict(svm_model, testset[,-1])
svm_tab <- table(pred = svm_prediction, true = testset[,1])
svm_tab
classAgreement(svm_tab)

bayes_model <- naiveBayes(trainset[,-1], trainset[,1])
summary(bayes_model)
bayes_prediction <- predict(bayes_model, testset[,-1])
bayes_tab <- table(pred = bayes_prediction, true = testset[,1])
bayes_tab
classAgreement(bayes_tab)