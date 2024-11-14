from flask import Blueprint,render_template,request,redirect,flash,url_for
from app.db.__init import Session,Pizza
from app.data.password import ADMIN_PASS


pizza_route = Blueprint("pizzas", __name__)

@pizza_route.get("/pizzas/")
@pizza_route.post("/pizzas/")
def add_pizza():
     with Session() as session:
        if request.method == "POST":
            name = request.form.get("name")
            price = request.form.get("price")
            pizza = Pizza(name=name,price=price)

            if request.form.get("password") == ADMIN_PASS:
                session.add(pizza)
                session.commit()
                flash("Піццу успішно додано")
                return redirect(url_for("pizzas.index"))
            else:
                flash("Нeвийшло додати піцу")

        return render_template("add_pizza.html")


@pizza_route.get("/pizza/del/<int:id>/")
def del_pizza(id):
    with Session() as session:
        pizza = session.query(Pizza).where(Pizza.id == id).first()
        session.delete(pizza)
        session.commit()
        return redirect(url_for("pizzas.index"))

@pizza_route.get("/")
def index():
     with Session() as session:
        pizzas = session.query(Pizza).all()
        return render_template("index.html", pizzas=pizzas)



@pizza_route.get("/pizza/edit/<int:id>")
@pizza_route.post("/pizza/edit/<int:id>")
def edit_pizza(id):
    with Session() as session:
        pizza = session.query(Pizza).where(Pizza.id == id).first()
        if request.method == "POST":
            name = request.form.get("name")
            price = request.form.get("price")

            pizza.name = name
            pizza.price = price
            session.commit()
            return redirect(url_for("pizzas.index"))

        return render_template("edit_pizza.html", pizza=pizza)

@pizza_route.get("/vote/")
def vote():
    question = "Яка піцца тобі подобається?"
    with Session() as session:
        pizzas = session.query(Pizza).all()
    return render_template("vote.html", question=question, pizzas=pizzas)


@pizza_route.get("/add_vote/")
def add_vote():
    vote = request.args.get("vote")
    with open("app/data/answers.txt", "a", encoding="utf-8") as file:
        file.write(vote + "\n")

    return redirect(url_for("pizzas.answers"))


@pizza_route.get("/answers/")
def answers():
    with open("app/data/answers.txt", "r", encoding="utf-8") as file:
        pizzas = file.readlines()

    return render_template("answers.html", pizzas=pizzas)
