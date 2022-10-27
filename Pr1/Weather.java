package Pr1;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Weather {
    public static void main(String[] args) throws IOException {
        List<Article> articleList = new ArrayList<>();
        Document doc = Jsoup.connect("http://travel.ru/weather/russia/").get();

        Elements trElements = doc.getElementsByAttributeValue("class", "b-table_row b-forecast");
        trElements.forEach(trElement ->{
            Elements elementsByClass = trElement.getElementsByClass("b-table_cell"); // выбираем элементы по классу b-table_cell
            System.out.print(elementsByClass.get(0).text() + " "); // первая колонка - Город
            // Парсим вторую колонку
            Element element = elementsByClass.get(1);
            String temp = element.getElementsByClass("b-forecast_temp").text(); // температура
            String precipitation = element.getElementsByClass("b-forecast_description").text(); // осадки
            System.out.println(temp + " " + precipitation);
        });
    }
}
class Article{
    private String url;
    private String name;

    public Article(String url,String name){
        this.url=url;
        this.name=name;
    }
    public String getUrl(){
        return url;
    }
    public void setUrl(){
        this.url=url;
    }
    public String getName(){
        return name;
    }
    public void setName(){
        this.name=name;
    }
}