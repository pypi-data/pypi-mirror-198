from django.conf import settings
from django.utils import translation

import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from .models import Group, Notification, Person
from .util.core_helpers import get_app_module, get_app_packages, has_person
from .util.frontend_helpers import get_language_cookie


class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification
        fields = [
            "sender",
            "recipient",
            "title",
            "description",
            "link",
            "icon",
            "send_at",
            "read",
            "sent",
            "created",
            "modified",
        ]

        @staticmethod
        def resolve_recipient(root, info, **kwargs):
            if info.context.user.has_perm("core.view_person_rule", root.recipient):
                return root.recipient
            raise PermissionDenied()


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = [
            "user",
            "first_name",
            "last_name",
            "additional_name",
            "short_name",
            "street",
            "housenumber",
            "postal_code",
            "place",
            "phone_number",
            "mobile_number",
            "email",
            "date_of_birth",
            "place_of_birth",
            "sex",
            "photo",
            "avatar",
            "guardians",
            "primary_group",
            "description",
            "children",
            "owner_of",
            "member_of",
        ]

    full_name = graphene.Field(graphene.String)

    def resolve_full_name(root: Person, info, **kwargs):
        return root.full_name

    def resolve_street(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_address_rule", root):
            return root.street
        return None

    def resolve_housenumber(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_address_rule", root):
            return root.housenumber
        return None

    def resolve_postal_code(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_address_rule", root):
            return root.postal_code
        return None

    def resolve_place(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_address_rule", root):
            return root.place
        return None

    def resolve_phone_number(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_contact_details_rule", root):
            return root.phone_number
        return None

    def resolve_mobile_number(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_contact_details_rule", root):
            return root.mobile_number
        return None

    def resolve_email(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_contact_details_rule", root):
            return root.email
        return None

    def resolve_date_of_birth(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_personal_details_rule", root):
            return root.date_of_birth
        return None

    def resolve_place_of_birth(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_personal_details_rule", root):
            return root.place_of_birth
        return None

    def resolve_children(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_personal_details_rule", root):
            return get_objects_for_user(info.context.user, "core.view_person", root.children.all())
        return []

    def resolve_guardians(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_personal_details_rule", root):
            return get_objects_for_user(info.context.user, "core.view_person", root.guardians.all())
        return []

    def resolve_member_of(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_person_groups_rule", root):
            return get_objects_for_user(info.context.user, "core.view_group", root.member_of.all())
        return []

    def resolve_owner_of(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_person_groups_rule", root):
            return get_objects_for_user(info.context.user, "core.view_group", root.owner_of.all())
        return []

    def resolve_primary_group(root, info, **kwargs):  # noqa
        if info.context.user.has_perm("core.view_group_rule", root.primary_group):
            return root.primary_group
        raise PermissionDenied()

    def resolve_photo(root, info, **kwargs):
        if info.context.user.has_perm("core.view_photo_rule", root):
            return root.photo
        return None

    def resolve_avatar(root, info, **kwargs):
        if info.context.user.has_perm("core.view_avatar_rule", root):
            return root.avatar
        return None


class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = [
            "name",
            "short_name",
            "members",
            "owners",
            "parent_groups",
            "group_type",
            "additional_fields",
            "photo",
            "avatar",
        ]

    @staticmethod
    def resolve_parent_groups(root, info, **kwargs):
        return get_objects_for_user(info.context.user, "core.view_group", root.parent_groups.all())

    @staticmethod
    def resolve_members(root, info, **kwargs):
        persons = get_objects_for_user(info.context.user, "core.view_person", root.members.all())
        if has_person(info.context.user) and [
            m for m in root.members.all() if m.pk == info.context.user.person.pk
        ]:
            persons = (persons | Person.objects.get(pk=info.context.user.person.pk)).distinct()
        return persons

    @staticmethod
    def resolve_owners(root, info, **kwargs):
        persons = get_objects_for_user(info.context.user, "core.view_person", root.owners.all())
        if has_person(info.context.user) and [
            o for o in root.owners.all() if o.pk == info.context.user.person.pk
        ]:
            persons = (persons | Person.objects.get(pk=info.context.user.person.pk)).distinct()
        return persons

    @staticmethod
    def resolve_group_type(root, info, **kwargs):
        if info.context.user.has_perm("core.view_grouptype_rule", root.group_type):
            return root.group_type
        raise PermissionDenied()

    @staticmethod
    def resolve_additional_fields(root, info, **kwargs):
        return get_objects_for_user(
            info.context.user, "core.view_additionalfield", root.additional_fields.all()
        )


class LanguageType(ObjectType):
    code = graphene.String(required=True)
    name = graphene.String(required=True)
    name_local = graphene.String(required=True)
    name_translated = graphene.String(required=True)
    bidi = graphene.Boolean(required=True)
    cookie = graphene.String(required=True)


class SystemPropertiesType(graphene.ObjectType):
    current_language = graphene.String(required=True)
    available_languages = graphene.List(LanguageType)

    def resolve_current_language(parent, info, **kwargs):
        return info.context.LANGUAGE_CODE

    def resolve_available_languages(parent, info, **kwargs):
        return [
            translation.get_language_info(code) | {"cookie": get_language_cookie(code)}
            for code, name in settings.LANGUAGES
        ]


class MarkNotificationReadMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()  # noqa

    notification = graphene.Field(NotificationType)

    @classmethod
    def mutate(cls, root, info, id):  # noqa
        notification = Notification.objects.get(pk=id, recipient=info.context.user.person)

        notification.read = True
        notification.save()

        return notification


class Query(graphene.ObjectType):
    ping = graphene.String(default_value="pong")

    who_am_i = graphene.Field(PersonType)

    system_properties = graphene.Field(SystemPropertiesType)

    def resolve_who_am_i(root, info, **kwargs):
        if has_person(info.context.user):
            return info.context.user.person
        else:
            return None

    def resolve_system_properties(root, info, **kwargs):
        return True


class Mutation(graphene.ObjectType):
    mark_notification_read = MarkNotificationReadMutation.Field()


def build_global_schema():
    """Build global GraphQL schema from all apps."""
    query_bases = [Query]
    mutation_bases = [Mutation]

    for app in get_app_packages():
        schema_mod = get_app_module(app, "schema")
        if not schema_mod:
            # The app does not define a schema
            continue

        if AppQuery := getattr(schema_mod, "Query", None):
            query_bases.append(AppQuery)
        if AppMutation := getattr(schema_mod, "Mutation", None):
            mutation_bases.append(AppMutation)

    # Define classes using all query/mutation classes as mixins
    #  cf. https://docs.graphene-python.org/projects/django/en/latest/schema/#adding-to-the-schema
    GlobalQuery = type("GlobalQuery", tuple(query_bases), {})
    GlobalMutation = type("GlobalMutation", tuple(mutation_bases), {})

    return graphene.Schema(query=GlobalQuery, mutation=GlobalMutation)


schema = build_global_schema()
