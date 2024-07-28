import { Burger, Center, Container, Group, Menu } from '@mantine/core'
import { useDisclosure } from '@mantine/hooks'
import { Link } from 'react-router-dom'
import classes from './Header.module.css'

const links = [
	{ link: '/', label: 'Телефоны' },
	{
		link: '#1',
		label: 'Learn',
		links: [
			{ link: '/docs', label: 'Documentation' },
			{ link: '/resources', label: 'Resources' },
			{ link: '/community', label: 'Community' },
			{ link: '/blog', label: 'Blog' },
		],
	},
	{ link: '/about', label: 'About' },
	{ link: '/pricing', label: 'Pricing' },
	{
		link: '#2',
		label: 'Support',
		links: [
			{ link: '/faq', label: 'FAQ' },
			{ link: '/demo', label: 'Book a demo' },
			{ link: '/forums', label: 'Forums' },
		],
	},
]

function HeaderMenu() {
	const [opened, { toggle }] = useDisclosure(false)

	const items = links.map(link => {
		const menuItems = link.links?.map(item => (
			<Menu.Item key={item.link}>{item.label}</Menu.Item>
		))

		if (menuItems) {
			return (
				<Menu
					key={link.label}
					trigger='hover'
					transitionProps={{ exitDuration: 0 }}
					withinPortal
				>
					<Menu.Target>
						<Link
							to={link.link}
							className={classes.link}
							onClick={event => event.preventDefault()}
						>
							<Center>
								<span className={classes.linkLabel}>{link.label}</span>
							</Center>
						</Link>
					</Menu.Target>
					<Menu.Dropdown>{menuItems}</Menu.Dropdown>
				</Menu>
			)
		}

		return (
			<a
				key={link.label}
				href={link.link}
				className={classes.link}
				onClick={event => event.preventDefault()}
			>
				{link.label}
			</a>
		)
	})

	return (
		<header className={classes.header}>
			<Container size='md'>
				<div className={classes.inner}>
					<h3>AndroidSender</h3>
					<Group gap={5} visibleFrom='sm'>
						{items}
					</Group>
					<Burger opened={opened} onClick={toggle} size='sm' hiddenFrom='sm' />
				</div>
			</Container>
		</header>
	)
}

export default HeaderMenu
