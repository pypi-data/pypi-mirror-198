# -*- coding: utf-8 -*-

"""
pokedream.help_command
~~~~~~~~~~~~~~~~~~~~

HelpCommand subclasses with pokedream features

:copyright: (c) 2021 ArnavPy (ArnavPy) R
:license: MIT, see LICENSE for more details.

"""

import typing

from discord.ext import commands

from pokedream.paginators import PaginatorEmbedInterface, PaginatorInterface


class DefaultPaginatorHelp(commands.DefaultHelpCommand):
    """
    A subclass of :class:`commands.DefaultHelpCommand` that uses a PaginatorInterface for pages.
    """

    def __init__(self, **options: typing.Any):
        paginator = options.pop('paginator', commands.Paginator(max_size=1980))

        super().__init__(paginator=paginator, **options)

    async def send_pages(self):
        destination = self.get_destination()

        interface = PaginatorInterface(self.context.bot, self.paginator, owner=self.context.author)
        await interface.send_to(destination)


class DefaultEmbedPaginatorHelp(commands.DefaultHelpCommand):
    """
    A subclass of :class:`commands.DefaultHelpCommand` that uses a PaginatorEmbedInterface for pages.
    """

    async def send_pages(self):
        destination = self.get_destination()

        interface = PaginatorEmbedInterface(self.context.bot, self.paginator, owner=self.context.author)
        await interface.send_to(destination)


class MinimalPaginatorHelp(commands.MinimalHelpCommand):
    """
    A subclass of :class:`commands.MinimalHelpCommand` that uses a PaginatorInterface for pages.
    """

    def __init__(self, **options: typing.Any):
        paginator = options.pop('paginator', commands.Paginator(prefix=None, suffix=None, max_size=1980))

        super().__init__(paginator=paginator, **options)

    async def send_pages(self):
        destination = self.get_destination()

        interface = PaginatorInterface(self.context.bot, self.paginator, owner=self.context.author)
        await interface.send_to(destination)


class MinimalEmbedPaginatorHelp(commands.MinimalHelpCommand):
    """
    A subclass of :class:`commands.MinimalHelpCommand` that uses a PaginatorEmbedInterface for pages.
    """

    async def send_pages(self):
        destination = self.get_destination()

        interface = PaginatorEmbedInterface(self.context.bot, self.paginator, owner=self.context.author)
        await interface.send_to(destination)
