#!/usr/bin/node

const len = process.argv.length - 2;

if (len === 0)
{
	console.log('No argument');
}
else
{
	console.log(process.argv[2]);
}
