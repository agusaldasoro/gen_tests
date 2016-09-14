#!/bin/bash
# Compile and run Daikon

mvn clean install
JAR_DIR=~/Documentos/gen_tests/taller-5
java -cp target/classes/:target/test-classes/:$JAR_DIR/daikon.jar:$JAR_DIR/junit-4.12.jar:$JAR_DIR/hamcrest-core-1.3.jar \
	daikon.Chicory \
	--daikon \
	--ppt-select-pattern="org.autotest.StackAr" \
	org.junit.runner.JUnitCore org.autotest.TestStackAr
