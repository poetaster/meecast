#include <QApplication>
#include <QGraphicsView>
#include <QGraphicsScene>
#include <QGraphicsWidget>
#include <QGraphicsLinearLayout>
#include <QDeclarativeComponent>
#include <QDeclarativeContext>
#include <QDeclarativeEngine>



#include "core.h"
#include "dataqml.h"


//////////////////////////////////////////////////////////////////////////////
DataQml *
create_and_fill_class_data_for_day_forecast()
{
    time_t      current_time, begin_current_day, end_current_day;
    struct tm   *tm = NULL;
    int         year, current_month;

    DataQml *wdata = new DataQml;
    /* Create current day */
    current_time = time(NULL);
    begin_current_day = current_time;
    tm = localtime(&begin_current_day);
    year = 1900 + tm->tm_year;
    current_month = tm->tm_mon;
    tm->tm_sec = 0; tm->tm_min = 0; tm->tm_hour = 0;
    tm->tm_isdst = 1;
    begin_current_day = mktime(tm);
    tm->tm_sec = 0; tm->tm_min = 59; tm->tm_hour = 23;
    end_current_day = mktime(tm);
    wdata->StartTime(begin_current_day);
    wdata->EndTime(end_current_day);
    wdata->Data::temperature().value(20.0);
    wdata->Flike(17.0);
    wdata->WindGust(2.8);
    wdata->WindSpeed(2.4);
    wdata->Humidity(845);
    wdata->Icon(4);
    wdata->Text(std::string("Cloudy"));
    return wdata;
}
//////////////////////////////////////////////////////////////////////////////

DataQml *
create_and_fill_class_data_for_hours_forecast()
{
    DataQml *wdata = new DataQml;
    wdata->StartTime(time(NULL) - 3600);
    wdata->EndTime(time(NULL) + 3600);
    wdata->Data::temperature().value(23.0);
    wdata->Flike(18.0);
    wdata->WindSpeed(3.0);
    wdata->WindGust(4.0);
    wdata->WindDirection(std::string("NNW"));
    wdata->Icon(3);
    wdata->Text(std::string("Clear"));
    return wdata;
}

int main(int argc, char* argv[])
{
    QApplication::setGraphicsSystem("native");
    QApplication app(argc, argv);



    //Set up a graphics scene with a QGraphicsWidget and Layout
    QGraphicsView view;
    QGraphicsScene scene;
    QGraphicsWidget *widget = new QGraphicsWidget();
    QGraphicsLinearLayout *layout = new QGraphicsLinearLayout();
    widget->setLayout(layout);
    scene.addItem(widget);
    view.setScene(&scene);


    //Add the QML snippet into the layout
    QDeclarativeEngine *engine = new QDeclarativeEngine;
    QDeclarativeComponent *c;
    QGraphicsLayoutItem* obj;

    DataQml *first = create_and_fill_class_data_for_hours_forecast();
    c = new QDeclarativeComponent(engine, QUrl(":weatherlayoutitem.qml"));
    obj = qobject_cast<QGraphicsLayoutItem*>(c->create());
    layout->addItem(obj);
    engine->rootContext()->setContextProperty("Forecast", first);

    DataQml *second =  create_and_fill_class_data_for_day_forecast();
    c = new QDeclarativeComponent(engine, QUrl(":weatherlayoutitem.qml"));
    obj = qobject_cast<QGraphicsLayoutItem*>(c->create());
    layout->addItem(obj);
    engine->rootContext()->setContextProperty("Forecast", second);


    widget->setGeometry(QRectF(0,0, 800,400));



    view.show();


    return app.exec();
}
