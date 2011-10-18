package controllers

import play._
import play.mvc._

object Application extends Controller {
    
    def index = {
        val widget1: Widget = Widget(1, "The first Widget")
        val widget2: Widget = Widget(2, "A really special Widget")
        val widget3: Widget = Widget(3, "Just another Widget")
        val widgets: Vector[Widget] = Vector(widget1, widget2, widget3)
        Json(widgets.toArray)
    }
    
}

case class Widget(val id: Int, val name: String)
