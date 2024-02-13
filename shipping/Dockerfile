FROM maven AS build
WORKDIR /app
RUN useradd roboshop
USER roboshop
ADD ./shipping/ .
RUN mvn dependency:resolve
RUN mvn package

FROM openjdk:8-jdk
EXPOSE 8080
WORKDIR /app
ENV CART_ENDPOINT=cart:8080
ENV DB_HOST=mysql
COPY --from=build /app/target/shipping-1.0.jar shipping.jar
CMD [ "java", "-Xmn256m", "-Xmx768m", "-jar", "shipping.jar" ]