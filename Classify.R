testset2 = read.csv('/users/nandu/desktop/PROJECT/Test.csv', head=FALSE)
trainset2 = read.csv('/users/nandu/desktop/PROJECT/Train.csv', head=FALSE)

tuned <- tune.svm(V1~., data = trainset2, gamma = 10^(-6:-1), cost = 10^(-1:1))
summary(tuned)
svm_model  <- svm(V1~., data = trainset2, kernel="radial", gamma=0.01, cost=10, probability=TRUE)
summary(svm_model)
svm_prediction <- predict(svm_model, testset2[,-1], decision.values = TRUE, probability = TRUE)
svm_tab <- table(pred = svm_prediction, true = testset2[,1])
svm_tab
classAgreement(svm_tab)

bayes_model <- naiveBayes(trainset2[,-1], trainset2[,1])
summary(bayes_model)
bayes_prediction <- predict(bayes_model, testset2[,-1])
bayes_tab <- table(pred = bayes_prediction, true = testset2[,1])
bayes_tab
classAgreement(bayes_tab)