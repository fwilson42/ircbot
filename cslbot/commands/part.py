# -*- coding: utf-8 -*-
# Copyright (C) 2013-2017 Samuel Damashek, Peter Foley, James Forcier, Srijay Kasturi, Reed Koser, Christopher Reffett, and Fox Wilson
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from ..helpers import arguments
from ..helpers.command import Command


@Command('part', ['handler', 'config', 'nick', 'type', 'target'], role="admin")
def cmd(send, msg, args):
    """Orders the bot to leave a channel
    Syntax: {command} <channel>
    """
    parser = arguments.ArgParser(args['config'])
    parser.add_argument('channel', nargs='+', action=arguments.ChanParser)
    try:
        cmdargs = parser.parse_args(msg)
    except arguments.ArgumentException as e:
        send(str(e))
        return
    for chan in cmdargs.channels:
        args['handler'].do_part(chan, args['nick'], args['target'], args['type'], send, args['handler'].connection)
