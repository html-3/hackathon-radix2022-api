from flask_marshmallow import Schema
from app.bid.models import Bid
from app.client_services.models import ClientServices
from app.student.models import Student
from app.task.models import Task
from app.tutor.models import Tutor
from app.utils.msg import msg
from werkzeug.datastructures import ImmutableMultiDict


class QueryInterface:
    """
    Object that bundles the search mechanism,
    parser, pagination, and filter. 
    """

    # Model mapping
    model = {
            "Task" : Task,
            "Student" : Student,
            "Tutor" : Tutor,
            "ClientServices" : ClientServices,
            "Bid" : Bid
            }
    
    # Fields able to be queried
    query_fields = {
            "Task" : 
                    [
                    Task.task_type,
                    Task.subject,
                    Task.knwlg_area,
                    ],
            "Student" : 
                    [
                    Student.name,
                    Student.email,
                    Student.cel_num,
                    ],
            "Tutor" : 
                    [
                    Tutor.name,
                    Tutor.email,
                    Tutor.cel_num,
                    ],
            "ClientServices" : 
                    [
                    ClientServices.name,
                    ClientServices.email,
                    ClientServices.cel_num,
                    ],
            "Bid" : # TODO adicionar novas opcoes de pesquisa pela alteracao do modelo das ofertas
                    # atualmente ocorre um erro no ORM (sqlalchemy.exc.ProgrammingError)
                    # por conta de bid_value ser um floar e task_id ser um inteiro
                    # deixar apenas uma opcao de pesquisa gera um erro no union dos queries (sqlalchemy.exc.ArgumentError)
                    # a alteracao atual foi feita para evitar esse tipo de erros
                    # adicionar Bid.task.subject, tambem nao funciona (AttributeError)
                    [
                    Bid.tutor_msg,
                    Bid.tutor_msg,
                    Bid.tutor_msg,
                    ]
            }
    
    @classmethod
    def search(cls, querystring : ImmutableMultiDict, query):
        """
        Returns a `QueryObject` filtered by the search parameters
        defined by the user.
        """

        search = querystring.get("search", "", type=str).strip()
        model_ref = query.column_descriptions[0].get("name")
        model_name = cls.query_fields.get(model_ref)
        queries = [0] * 3

        if model_ref == "Task":
            for task in query.all(): task.check_status()

        if search != "":
            if query.column_descriptions[0].get("name") in ["Task", "Student", "Tutor", "Admin", "ClientServices", "Bid"]:
                for i, q in enumerate(model_name):
                    queries[i] = query.filter(q.ilike(f"%{search}%"))

            else:
                msg(400, "Ocorreu um erro na sua pesquisa!")

            try:
                query = query.where(cls.model.get(model_ref).id == int(search))
                filter_out = query.union_all(*queries)
            except ValueError:
                filter_out = queries[0].union_all(*queries[1:])

            return filter_out
        else:
            return query
            

    @classmethod
    def parse(cls, querystring : ImmutableMultiDict, query):
        """
        Returns a `QueryObject` parsed by the search parameters
        defined by the user.
        """

        model = cls.model.get(query.column_descriptions[0].get("name"))
        status = querystring.get("status", "", type=str).strip()
        try:
            return query.filter(model.status.ilike(f"%{status}%"))
        except AttributeError:
            return query

        

    @staticmethod
    def paginate(querystring : ImmutableMultiDict, query, per_page : int = 30):
        """
        Returns the length, last page and items of a
        paginated `QueryObject`.
        """

        page = querystring.get("page", 1, type=int)
        per_page = querystring.get("per_page", per_page, type=int)

        pagination_length = len(query.all())
        last_page = pagination_length // per_page + 1
        query = query.paginate(page=page, per_page=per_page).items


        return pagination_length, last_page, query

    @staticmethod
    def filter(many, querystring : ImmutableMultiDict,  schema : Schema, exclude : list = [], **kwargs):
        """
        Returns a marshmallow `Schema` object that filters
        a object when serializing.
        """

        include = querystring.get("include", None)

        if not include:
            try:
                schema_out = schema(many=many, exclude=exclude, **kwargs)
            except ValueError:
                msg(400, "Campo inválido")

        else:
            include_out = include.split(",") if include else None
            only = list(set(include_out) - set(exclude))
            try:
                schema_out = schema(many=many, only=only, **kwargs)
            except ValueError:
                msg(400, "Campo inválido")

        return schema_out

    @classmethod
    def sort(cls, qs):
        pass

    """@classmethod
    def many(cls, qs, query, schema, exclude, **kwarg):
        search = cls.search(qs,query)
        parse = cls.parse(qs, search)
        quantity, last_page, items = cls.paginate(qs, parse)
        schema = cls.filter(qs, schema, exclude)

        msg(
            200, "Ok!", 
            quantity=quantity, 
            last_page=last_page,
            items=schema.dump(items))"""

    @classmethod
    def serialize(cls, many : bool, qs, query, schema, exclude, **kwarg):
        """
        Dumps a serialized object or objects. If `many = True`,
        it searches, parses, paginates, and filters the serilization.
        """
        if many:
            search = cls.search(qs, query, **kwarg)
            parse = cls.parse(qs, search, **kwarg)
            quantity, last_page, items = cls.paginate(qs, parse, **kwarg)
            schema = cls.filter(many, qs, schema, exclude, **kwarg)

            make_response(
                200, "Ok!", 
                ver1=False,
                quantity=quantity, 
                last_page=last_page,
                items=schema.dump(items)
                )

        else:
            schema = cls.filter(many, qs, schema, exclude)

            msg(
                200, "Ok!",
                ver1=False,
                **schema.dump(query)
                )

out = QueryInterface()




            
